"""
Aria - Wikipedia Scraper Module
Fetches real-time summaries from Wikipedia for factual queries not found
in the fixed Q&A dataset.

Approach:
1. Use Wikipedia's OpenSearch endpoint to resolve the user's messy query
   into the correct article title.
2. If that fails for any reason, fall back to guessing the direct page
   URL from the cleaned search term.
3. Fetch the resolved page's HTML and use BeautifulSoup to extract a
   clean summary from the actual page content (the scraping step).

Debug prints are included (visible in the terminal when running
chatbot.py) so any failure reason is visible instead of a silent fail.
"""

import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AriaChatBot/1.0 "
                  "(InternGrow Internship Project; contact: student project)"
}

OPENSEARCH_URL = "https://en.wikipedia.org/w/api.php"
SUMMARY_SENTENCE_LIMIT = 3
DEBUG = True  # Set to False later to silence terminal debug prints

NON_FACTUAL_STARTERS = [
    "write me", "write a", "should i", "can you write", "give me a poem",
    "how do i feel", "what should i do", "make me a", "create a story",
    "i think", "do you love", "will you marry"
]


def _log(*args):
    if DEBUG:
        print("[wiki_scraper]", *args)


def _clean_query(query: str) -> str:
    filler_words = [
        "what is", "what are", "who is", "who are", "who was", "tell me about",
        "explain", "define", "meaning of", "batao", "kya hai", "kaun hai",
        "kaun tha", "kya hota hai", "bataiye", "history of", "information about"
    ]
    cleaned = query.lower().strip()
    for filler in filler_words:
        cleaned = cleaned.replace(filler, "")
    return cleaned.strip(" ?.!")


def _looks_non_factual(query: str) -> bool:
    q = query.lower()
    return any(q.startswith(starter) for starter in NON_FACTUAL_STARTERS)


def _resolve_title_via_opensearch(search_term: str):
    """Primary method: ask Wikipedia's OpenSearch API for the best title."""
    try:
        response = requests.get(
            OPENSEARCH_URL,
            params={
                "action": "opensearch",
                "search": search_term,
                "limit": 1,
                "namespace": 0,
                "format": "json"
            },
            headers=HEADERS,
            timeout=8
        )
        _log("OpenSearch status code:", response.status_code)
        response.raise_for_status()
        data = response.json()
        titles = data[1]
        urls = data[3]
        if titles:
            _log("OpenSearch resolved title:", titles[0])
            return titles[0], urls[0]
        _log("OpenSearch returned no titles for:", search_term)
        return None, None
    except Exception as e:
        _log("OpenSearch failed with error:", repr(e))
        return None, None


def _resolve_title_direct_guess(search_term: str):
    """Fallback method: guess the direct Wikipedia URL from the search term."""
    guessed_title = search_term.title()
    page_url = f"https://en.wikipedia.org/wiki/{guessed_title.replace(' ', '_')}"
    try:
        response = requests.head(page_url, headers=HEADERS, timeout=8, allow_redirects=True)
        _log("Direct-guess status code:", response.status_code, "for", page_url)
        if response.status_code == 200:
            return guessed_title, response.url
        return None, None
    except Exception as e:
        _log("Direct-guess failed with error:", repr(e))
        return None, None


def _extract_summary(soup: BeautifulSoup) -> str:
    # Try the most common container first, then fall back progressively.
    # Using descendant search (not strict direct-child) so it survives
    # Wikipedia skin/markup changes that add extra wrapper divs.
    content_container = soup.select_one("#mw-content-text .mw-parser-output")
    if not content_container:
        content_container = soup.select_one("#mw-content-text")
    if not content_container:
        content_container = soup

    paragraphs = content_container.find_all("p")
    _log(f"Found {len(paragraphs)} paragraph tags on page")

    for para in paragraphs:
        # Remove citation superscripts like [1], [2] before extracting text
        for sup_tag in para.select("sup.reference"):
            sup_tag.decompose()

        # Use a space separator so text from adjacent inline tags
        # (links, italics, etc.) doesn't run together
        text = para.get_text(separator=" ", strip=True)

        # Collapse repeated whitespace
        text = re.sub(r"\s+", " ", text)
        # Remove stray space before punctuation (e.g. "word ," -> "word,")
        text = re.sub(r"\s+([.,;:)])", r"\1", text)
        # Remove stray space after an opening parenthesis
        text = re.sub(r"([(])\s+", r"\1", text)

        if len(text) > 40:
            sentences = text.split(". ")
            summary = ". ".join(sentences[:SUMMARY_SENTENCE_LIMIT])
            if not summary.endswith("."):
                summary += "."
            return summary

    return ""


def get_wikipedia_summary(query: str) -> dict:
    _log("Query received:", query)

    if _looks_non_factual(query):
        _log("Flagged as non-factual, skipping Wikipedia")
        return {"success": False, "error": "non_factual"}

    search_term = _clean_query(query)
    _log("Cleaned search term:", search_term)

    if not search_term:
        return {"success": False, "error": "empty_query"}

    try:
        # Step 1: Try OpenSearch first
        title, page_url = _resolve_title_via_opensearch(search_term)

        # Step 2: Fall back to direct URL guess if OpenSearch didn't work
        if not title:
            _log("Falling back to direct-guess method")
            title, page_url = _resolve_title_direct_guess(search_term)

        if not title:
            _log("Both resolution methods failed — no article found")
            return {"success": False, "error": "no_content"}

        # Step 3: Fetch the page and scrape it with BeautifulSoup
        response = requests.get(page_url, headers=HEADERS, timeout=8)
        _log("Page fetch status code:", response.status_code)
        _log("Page HTML length:", len(response.text))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        _log("mw-parser-output found on page:", soup.select_one(".mw-parser-output") is not None)

        if soup.find(id="disambigbox"):
            _log("Disambiguation page detected")
            return {
                "success": False,
                "error": "disambiguation",
                "message": "Ye query multiple cheezon se match karti hai, thora specific poochein."
            }

        summary = _extract_summary(soup)
        if not summary:
            _log("No usable summary extracted from page")
            return {"success": False, "error": "no_content"}

        _log("Summary successfully extracted, length:", len(summary))
        return {
            "success": True,
            "title": title,
            "summary": summary,
            "url": page_url
        }

    except requests.exceptions.Timeout:
        _log("Request timed out")
        return {"success": False, "error": "timeout"}
    except requests.exceptions.RequestException as e:
        _log("Network error:", repr(e))
        return {"success": False, "error": "network_error", "details": str(e)}


if __name__ == "__main__":
    test_queries = [
        "gravity",
        "what is gravity",
        "who is elon musk",
        "quantam physicss",
        "write me a poem",
        "asdkjaskldjaskld"
    ]
    for q in test_queries:
        print(f"\n{'=' * 50}\nQuery: {q}")
        print(get_wikipedia_summary(q))
