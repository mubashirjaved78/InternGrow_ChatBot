"""
Aria - AI Assistant 
A professional, modern-themed rule-based chatbot with Wikipedia scraping fallback.

Task 4: Intelligent Rule-Based Assistant (InternGrow Python Programming Track)

Features:
- Typing animation (letter-by-letter bot replies)
- Dark / Light theme toggle
- Clear chat + Export chat to .txt
- Subtle sound effects on send/receive
- Custom app icon
- Quick-suggestion chips

Author: Mubashir Javed
"""

import tkinter as tk
from tkinter import font, filedialog, messagebox
import threading
import random
import os
from datetime import datetime

from qa_dataset import QA_DATABASE
from wiki_scraper import get_wikipedia_summary

try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False


BOT_NAME = "Aria"
SUGGESTION_CHIPS = ["👋 Say Hi", "😂 Tell me a joke", "💡 Motivate me", "🌍 What is AI?"]


# THEMES (Dark + Light palettes)
THEMES = {
    "dark": {
        "bg": "#0f0f1a",
        "header_1": "#6366f1",
        "header_2": "#8b5cf6",
        "header_shadow": "#4c1d95",
        "chat_bg": "#14141f",
        "input_bar_bg": "#1a1a29",
        "input_field_bg": "#24243a",
        "user_bubble": "#6366f1",
        "bot_bubble": "#24243a",
        "user_text": "#ffffff",
        "bot_text": "#e4e4f0",
        "accent": "#a78bfa",
        "send_btn": "#6366f1",
        "send_btn_hover": "#7b7ff5",
        "timestamp": "#5c5c78",
        "title_text": "#ffffff",
        "subtitle_text": "#d8d8f8",
        "status_dot": "#4ade80",
        "chip_bg": "#1e1e30",
        "chip_border": "#3a3a5c",
        "chip_hover": "#2a2a45",
        "bubble_shadow": "#0a0a12",
        "avatar_ring": "#c4b5fd",
        "icon_btn": "#e4e4f0",
        "icon_btn_hover": "#ffffff",
    },
    "light": {
        "bg": "#f4f4fb",
        "header_1": "#6366f1",
        "header_2": "#8b5cf6",
        "header_shadow": "#c7d2fe",
        "chat_bg": "#ffffff",
        "input_bar_bg": "#f0f0fa",
        "input_field_bg": "#e9e9f7",
        "user_bubble": "#6366f1",
        "bot_bubble": "#eeeef7",
        "user_text": "#ffffff",
        "bot_text": "#26263a",
        "accent": "#6d28d9",
        "send_btn": "#6366f1",
        "send_btn_hover": "#7b7ff5",
        "timestamp": "#8888a0",
        "title_text": "#ffffff",
        "subtitle_text": "#eeeeff",
        "status_dot": "#22c55e",
        "chip_bg": "#eeeef7",
        "chip_border": "#c7c7e5",
        "chip_hover": "#e0e0f5",
        "bubble_shadow": "#d8d8ee",
        "avatar_ring": "#a78bfa",
        "icon_btn": "#4c4c66",
        "icon_btn_hover": "#1e1e2e",
    }
}

# BILINGUAL SYSTEM STRINGS (Roman Urdu / English)
# Note: this covers Aria's own generated messages (welcome, errors,
# Wikipedia intro line). The 250+ fixed Q&A dataset responses stay in
# Roman Urdu — translating all of those is a separate, larger task.
STRINGS = {
    "ur": {
        "welcome": (
            "Assalam o Alaikum! Main {name} hoon ✨\n\n"
            "Main aapki 3 tareeke se madad kar sakti hoon:\n"
            "• General chit-chat aur greetings\n"
            "• Motivation, jokes, aur fun facts\n"
            "• Factual sawal — agar mujhe pata na hua, Wikipedia se dhoondh kar bataungi!\n\n"
            "Chaliye shuru karte hain 👇"
        ),
        "wiki_intro": "Mujhe pehle se iska jawab nahi pata tha, to maine Wikipedia se dekha!",
        "err_disambiguation": "Ye query multiple cheezon se match karti hai, thora specific poochein.",
        "err_timeout": "Sorry, internet thora slow lag raha hai, dobara try karein.",
        "err_network": "Internet connection check karein, Wikipedia tak pohanchne mein masla ho raha hai.",
        "err_non_factual": ("Ye sawal thora open-ended/creative lag raha hai — main ek rule-based "
                             "bot hoon jo factual/encyclopedia info Wikipedia se la sakti hoon, "
                             "lekin ChatGPT jaisi creative writing ya opinions nahi de sakti. "
                             "Koi factual sawal poochein, jaise 'what is gravity' ya 'who is Einstein'."),
        "err_generic": "Sorry, mujhe iska jawab nahi mila. Thora alfaz badal kar dobara poochein?",
        "clear_confirm_title": "Clear Chat",
        "clear_confirm_msg": "Poori chat clear karna chahte hain?",
        "export_empty": "Abhi koi messages nahi hain export karne ke liye.",
        "export_success": "Chat successfully export ho gayi!",
        "export_error": "Export nahi ho saka: {error}",
    },
    "en": {
        "welcome": (
            "Hello! I'm {name} ✨\n\n"
            "I can help you in 3 ways:\n"
            "• General chit-chat and greetings\n"
            "• Motivation, jokes, and fun facts\n"
            "• Factual questions — if I don't know, I'll look it up on Wikipedia!\n\n"
            "Let's get started 👇"
        ),
        "wiki_intro": "I didn't know this one already, so I looked it up on Wikipedia!",
        "err_disambiguation": "This query matches multiple topics — could you be more specific?",
        "err_timeout": "Sorry, the connection seems slow right now, please try again.",
        "err_network": "Please check your internet connection — I couldn't reach Wikipedia.",
        "err_non_factual": ("That sounds a bit open-ended or creative — I'm a rule-based bot "
                             "that pulls factual/encyclopedia info from Wikipedia, but I can't "
                             "do ChatGPT-style creative writing or share opinions. "
                             "Try a factual question, like 'what is gravity' or 'who is Einstein'."),
        "err_generic": "Sorry, I couldn't find an answer for that. Try rephrasing it?",
        "clear_confirm_title": "Clear Chat",
        "clear_confirm_msg": "Are you sure you want to clear the entire chat?",
        "export_empty": "There are no messages to export yet.",
        "export_success": "Chat exported successfully!",
        "export_error": "Export failed: {error}",
    }
}


# CHATBOT LOGIC (Brain)
class ChatbotEngine:
    """Handles matching user input to responses, with Wikipedia fallback."""

    def __init__(self):
        self.qa_database = QA_DATABASE

    def get_response(self, user_input: str, language: str = "ur") -> str:
        user_input_clean = user_input.lower().strip()

        matched_response = self._match_dataset(user_input_clean, language)
        if matched_response:
            return matched_response

        return self._get_wiki_response(user_input, language)

    def _match_dataset(self, user_input: str, language: str = "ur"):
        best_match = None
        best_match_length = 0

        for entry in self.qa_database:
            for pattern in entry["patterns"]:
                if pattern in user_input:
                    if len(pattern) > best_match_length:
                        best_match = entry
                        best_match_length = len(pattern)

        if best_match:
            response_key = f"responses_{language}"
            # Fallback to Roman Urdu responses if a language key is ever missing
            responses = best_match.get(response_key, best_match.get("responses_ur", []))
            if responses:
                return random.choice(responses)
        return None

    def _get_wiki_response(self, user_input: str, language: str = "ur") -> str:
        s = STRINGS[language]
        result = get_wikipedia_summary(user_input)

        if result.get("success"):
            title = result["title"]
            summary = result["summary"]
            return f"{s['wiki_intro']}\n\n📖 {title}\n{summary}"

        error = result.get("error")
        if error == "disambiguation":
            return s["err_disambiguation"]
        elif error == "timeout":
            return s["err_timeout"]
        elif error == "network_error":
            return s["err_network"]
        elif error == "non_factual":
            return s["err_non_factual"]
        else:
            return s["err_generic"]


# ROUNDED RECTANGLE HELPER
def draw_rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [
        x1 + radius, y1, x2 - radius, y1, x2, y1, x2, y1 + radius,
        x2, y2 - radius, x2, y2, x2 - radius, y2, x1 + radius, y2,
        x1, y2, x1, y2 - radius, x1, y1 + radius, x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


# GUI APPLICATION
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.engine = ChatbotEngine()
        self.theme_name = "dark"
        self.language = "ur"
        self.colors = THEMES[self.theme_name]
        self.message_log = []  
        self._setup_window()
        self._setup_fonts()
        self._build_header()
        self._build_chat_area()
        self._build_input_area()
        self._show_welcome_message()

    # -------------------- SETUP --------------------
    def _setup_window(self):
        self.root.title(f"{BOT_NAME} — AI Assistant")
        self.root.geometry("520x720")
        self.root.minsize(420, 550)
        self.root.configure(bg=self.colors["bg"])
        self._set_app_icon()

    def _set_app_icon(self):
        try:
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aria_icon.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception:
            pass  # Icon is a nice-to-have; don't crash if unavailable on this OS

    def _setup_fonts(self):
        self.font_title = font.Font(family="Segoe UI", size=16, weight="bold")
        self.font_subtitle = font.Font(family="Segoe UI", size=9)
        self.font_message = font.Font(family="Segoe UI", size=10)
        self.font_timestamp = font.Font(family="Segoe UI", size=7)
        self.font_chip = font.Font(family="Segoe UI", size=9)
        self.font_icon_btn = font.Font(family="Segoe UI", size=13)

    # -------------------- HEADER --------------------
    def _build_header(self):
        self.header_height = 96
        self.header_canvas = tk.Canvas(self.root, height=self.header_height,
                                        highlightthickness=0, bg=self.colors["header_1"])
        self.header_canvas.pack(fill="x", side="top")
        self.header_canvas.bind("<Configure>", self._redraw_header)
        self.header_canvas.bind("<Button-1>", self._on_header_click)

    def _redraw_header(self, event=None):
        width = event.width if event else self.header_canvas.winfo_width()
        if width < 2:
            return
        self.header_canvas.delete("all")
        c = self.colors

        steps = 80
        c1 = self._hex_to_rgb(c["header_1"])
        c2 = self._hex_to_rgb(c["header_2"])
        step_width = width / steps
        for i in range(steps):
            ratio = i / steps
            r = int(c1[0] + (c2[0] - c1[0]) * ratio)
            g = int(c1[1] + (c2[1] - c1[1]) * ratio)
            b = int(c1[2] + (c2[2] - c1[2]) * ratio)
            color = f"#{r:02x}{g:02x}{b:02x}"
            x0 = i * step_width
            x1 = x0 + step_width + 1
            self.header_canvas.create_rectangle(x0, 0, x1, self.header_height,
                                                 fill=color, outline=color)

        self.header_canvas.create_rectangle(0, self.header_height - 3, width,
                                             self.header_height, fill=c["header_shadow"],
                                             outline="")

        # ---- Reserve a zone on the right for icon buttons, center the
        # avatar+title block within the remaining left area ----
        buttons_zone_width = 190
        avail_width = max(width - buttons_zone_width, 220)
        block_width = 210
        block_start_x = max(16, (avail_width - block_width) / 2)

        avatar_x, avatar_y, avatar_r = block_start_x + 26, 48, 26
        self.header_canvas.create_oval(
            avatar_x - avatar_r - 3, avatar_y - avatar_r - 3,
            avatar_x + avatar_r + 3, avatar_y + avatar_r + 3,
            fill="", outline=c["avatar_ring"], width=2
        )
        self.header_canvas.create_oval(
            avatar_x - avatar_r, avatar_y - avatar_r,
            avatar_x + avatar_r, avatar_y + avatar_r,
            fill="#ffffff", outline=""
        )
        self.header_canvas.create_text(avatar_x, avatar_y, text="✨",
                                        font=("Segoe UI Emoji", 22))

        text_x = avatar_x + avatar_r + 16
        self.header_canvas.create_text(
            text_x, 34, text=BOT_NAME, font=self.font_title,
            fill=c["title_text"], anchor="w"
        )

        self.header_canvas.create_oval(text_x + 2, 60, text_x + 11, 69,
                                        fill=c["status_dot"], outline="")
        self.header_canvas.create_text(
            text_x + 16, 64, text="Online • AI Assistant", font=self.font_subtitle,
            fill=c["subtitle_text"], anchor="w"
        )

        # ---- Circular icon buttons (top-right): Clear, Export, Theme, Language ----
        theme_icon = "☀" if self.theme_name == "dark" else "🌙"
        lang_icon = "🌐"
        self.header_buttons = [
            ("clear", "🗑", "#ef4444"),
            ("export", "⤓", None),
            ("theme", theme_icon, None),
            ("language", lang_icon, None),
        ]
        btn_radius = 18
        btn_y = 30
        btn_gap = 44
        self._header_btn_positions = {}

        for i, (key, icon, accent_color) in enumerate(self.header_buttons):
            bx = width - 28 - i * btn_gap
            self._header_btn_positions[key] = bx
            self.header_canvas.create_oval(
                bx - btn_radius, btn_y - btn_radius, bx + btn_radius, btn_y + btn_radius,
                fill="#ffffff", outline="", stipple="gray50"
            )
            self.header_canvas.create_text(bx, btn_y, text=icon, font=("Segoe UI Emoji", 13))

        label_map = {
            "clear": "Clear", "export": "Save", "theme": "Theme",
            "language": "اردو" if self.language == "ur" else "EN"
        }
        for i, (key, _, _) in enumerate(self.header_buttons):
            bx = width - 28 - i * btn_gap
            label = label_map.get(key, "")
            self.header_canvas.create_text(bx, btn_y + 22, text=label, font=("Segoe UI", 6),
                                            fill=c["subtitle_text"])

    def _on_header_click(self, event):
        width = self.header_canvas.winfo_width()
        x, y = event.x, event.y
        if y > 50 or not hasattr(self, "_header_btn_positions"):
            return
        for key, bx in self._header_btn_positions.items():
            if bx - 20 <= x <= bx + 20:
                if key == "theme":
                    self._toggle_theme()
                elif key == "export":
                    self._export_chat()
                elif key == "clear":
                    self._clear_chat()
                elif key == "language":
                    self._toggle_language()
                return

    @staticmethod
    def _hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    # -------------------- THEME TOGGLE --------------------
    def _toggle_theme(self):
        self.theme_name = "light" if self.theme_name == "dark" else "dark"
        self.colors = THEMES[self.theme_name]
        self._apply_theme()

    def _apply_theme(self):
        c = self.colors
        self.root.configure(bg=c["bg"])
        self._redraw_header()
        self.chat_canvas.configure(bg=c["chat_bg"])
        self.chat_frame.configure(bg=c["chat_bg"])
        self.input_container.configure(bg=c["input_bar_bg"])
        self.input_inner.configure(bg=c["input_bar_bg"])
        self.field_frame.configure(bg=c["input_field_bg"])
        self.entry.configure(bg=c["input_field_bg"], fg=c["bot_text"],
                              insertbackground=c["bot_text"])
        self.send_btn.configure(bg=c["input_bar_bg"])
        self._draw_send_button(c["send_btn"])
        self._render_all_messages()

    # -------------------- LANGUAGE TOGGLE --------------------
    def _toggle_language(self):
        self.language = "en" if self.language == "ur" else "ur"
        self._redraw_header()
        # Future bot replies (system messages) will use the new language.
        # Past messages in the chat log are left as originally sent.

    # -------------------- CHAT AREA --------------------
    def _build_chat_area(self):
        container = tk.Frame(self.root, bg=self.colors["chat_bg"])
        container.pack(fill="both", expand=True)

        self.chat_canvas = tk.Canvas(container, bg=self.colors["chat_bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=self.chat_canvas.yview)
        self.chat_frame = tk.Frame(self.chat_canvas, bg=self.colors["chat_bg"])

        self.chat_frame.bind(
            "<Configure>",
            lambda e: self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))
        )

        self.canvas_window = self.chat_canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
        self.chat_canvas.configure(yscrollcommand=scrollbar.set)
        self.chat_canvas.bind("<Configure>", self._on_canvas_resize)

        self.chat_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.chat_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_canvas_resize(self, event):
        self.chat_canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        self.chat_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # -------------------- INPUT AREA --------------------
    def _build_input_area(self):
        c = self.colors
        self.input_container = tk.Frame(self.root, bg=c["input_bar_bg"], height=70)
        self.input_container.pack(fill="x", side="bottom")
        self.input_container.pack_propagate(False)

        self.input_inner = tk.Frame(self.input_container, bg=c["input_bar_bg"])
        self.input_inner.pack(fill="both", expand=True, padx=14, pady=12)

        self.field_frame = tk.Frame(self.input_inner, bg=c["input_field_bg"])
        self.field_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

        self.entry = tk.Entry(self.field_frame, font=self.font_message, bg=c["input_field_bg"],
                               fg=c["bot_text"], insertbackground=c["bot_text"],
                               relief="flat", bd=0)
        self.entry.pack(fill="both", expand=True, ipady=12, padx=14)
        self.entry.bind("<Return>", lambda e: self._send_message())
        self.entry.focus_set()

        self.send_btn = tk.Canvas(self.input_inner, width=48, height=48, bg=c["input_bar_bg"],
                                   highlightthickness=0, cursor="hand2")
        self.send_btn.pack(side="right")
        self._draw_send_button(c["send_btn"])
        self.send_btn.bind("<Button-1>", lambda e: self._send_message())
        self.send_btn.bind("<Enter>", lambda e: self._draw_send_button(self.colors["send_btn_hover"]))
        self.send_btn.bind("<Leave>", lambda e: self._draw_send_button(self.colors["send_btn"]))

    def _draw_send_button(self, color):
        self.send_btn.delete("all")
        self.send_btn.create_oval(2, 2, 46, 46, fill=color, outline="")
        self.send_btn.create_text(24, 24, text="➤", font=("Segoe UI", 14, "bold"), fill="white")

    # -------------------- MESSAGE BUBBLES --------------------
    def _add_bubble(self, text, is_user=False, animate=False):
        c = self.colors
        row = tk.Frame(self.chat_frame, bg=c["chat_bg"])
        row.pack(fill="x", pady=6, padx=14, anchor="e" if is_user else "w")

        bubble_color = c["user_bubble"] if is_user else c["bot_bubble"]
        text_color = c["user_text"] if is_user else c["bot_text"]

        max_width_chars = 42
        wrapped_lines = self._wrap_text(text, max_width_chars)
        line_count = len(wrapped_lines)
        line_height_px = 19

        longest_line_px = max(self.font_message.measure(l) for l in wrapped_lines)
        bubble_width = min(340, max(70, longest_line_px + 32))
        bubble_height = line_count * line_height_px + 26

        canvas = tk.Canvas(row, width=bubble_width + 4, height=bubble_height + 4,
                            bg=c["chat_bg"], highlightthickness=0)
        canvas.pack(side="right" if is_user else "left")

        draw_rounded_rect(canvas, 4, 5, bubble_width, bubble_height + 1,
                           radius=16, fill=c["bubble_shadow"], outline="")
        draw_rounded_rect(canvas, 2, 2, bubble_width - 2, bubble_height - 1,
                           radius=16, fill=bubble_color, outline="")

        text_item = canvas.create_text(16, (bubble_height + 4) / 2, text="",
                                        font=self.font_message, fill=text_color,
                                        anchor="w", justify="left")

        ts_row = tk.Frame(self.chat_frame, bg=c["chat_bg"])
        ts_row.pack(fill="x", padx=18, anchor="e" if is_user else "w")
        tk.Label(ts_row, text=datetime.now().strftime("%I:%M %p"),
                 font=self.font_timestamp, bg=c["chat_bg"],
                 fg=c["timestamp"]).pack(side="right" if is_user else "left")

        full_text = "\n".join(wrapped_lines)
        if animate:
            self._animate_text(canvas, text_item, full_text)
        else:
            canvas.itemconfig(text_item, text=full_text)

        self.root.after(50, self._scroll_to_bottom)

    def _animate_text(self, canvas, text_item, full_text, index=0):
        """Reveals the bot's message a few characters at a time (typing effect)."""
        step = 2  # characters revealed per tick — smooth but not sluggish
        if index >= len(full_text):
            canvas.itemconfig(text_item, text=full_text)
            return
        next_index = min(index + step, len(full_text))
        canvas.itemconfig(text_item, text=full_text[:next_index])
        self.root.after(12, lambda: self._animate_text(canvas, text_item, full_text, next_index))
        self.root.after(12, self._scroll_to_bottom)

    @staticmethod
    def _wrap_text(text, max_chars):
        wrapped = []
        for paragraph in text.split("\n"):
            if not paragraph:
                wrapped.append("")
                continue
            words = paragraph.split(" ")
            line = ""
            for word in words:
                if len(line) + len(word) + 1 <= max_chars:
                    line = f"{line} {word}".strip()
                else:
                    wrapped.append(line)
                    line = word
            if line:
                wrapped.append(line)
        return wrapped if wrapped else [""]

    def _scroll_to_bottom(self):
        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)

    # -------------------- RENDER / RE-RENDER --------------------
    def _render_all_messages(self):
        """Clears and redraws every message from the log — used after a theme switch."""
        for widget in self.chat_frame.winfo_children():
            widget.destroy()

        log_copy = list(self.message_log)
        self.message_log = []
        for text, is_user in log_copy:
            self._add_bubble(text, is_user=is_user, animate=False)
            self.message_log.append((text, is_user))

        if not log_copy:
            self._show_welcome_message(record=False)
        else:
            self._show_suggestion_chips()

        self.root.after(50, self._scroll_to_bottom)

    def _show_welcome_message(self, record=True):
        welcome_text = STRINGS[self.language]["welcome"].format(name=BOT_NAME)
        self._add_bubble(welcome_text, is_user=False)
        if record:
            self.message_log.append((welcome_text, False))
        self._show_suggestion_chips()

    # -------------------- SUGGESTION CHIPS --------------------
    def _show_suggestion_chips(self):
        c = self.colors
        chip_row = tk.Frame(self.chat_frame, bg=c["chat_bg"])
        chip_row.pack(fill="x", padx=14, pady=(4, 10), anchor="w")

        wrap_frame = tk.Frame(chip_row, bg=c["chat_bg"])
        wrap_frame.pack(anchor="w")

        for i, chip_text in enumerate(SUGGESTION_CHIPS):
            chip = tk.Label(wrap_frame, text=chip_text, font=self.font_chip,
                             bg=c["chip_bg"], fg=c["accent"], padx=16, pady=9,
                             cursor="hand2", relief="flat",
                             highlightbackground=c["chip_border"],
                             highlightthickness=1)
            chip.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="w")
            chip.bind("<Enter>", lambda e, ch=chip: ch.config(bg=self.colors["chip_hover"]))
            chip.bind("<Leave>", lambda e, ch=chip: ch.config(bg=self.colors["chip_bg"]))
            chip.bind("<Button-1>", lambda e, t=chip_text: self._send_chip(t))

    def _send_chip(self, chip_text):
        clean_text = chip_text.split(" ", 1)[1] if " " in chip_text else chip_text
        self.entry.delete(0, tk.END)
        self.entry.insert(0, clean_text)
        self._send_message()

    # -------------------- TYPING INDICATOR --------------------
    def _show_typing_indicator(self):
        c = self.colors
        self.typing_row = tk.Frame(self.chat_frame, bg=c["chat_bg"])
        self.typing_row.pack(fill="x", pady=6, padx=14, anchor="w")

        canvas = tk.Canvas(self.typing_row, width=90, height=36,
                            bg=c["chat_bg"], highlightthickness=0)
        canvas.pack(side="left")
        draw_rounded_rect(canvas, 2, 2, 88, 34, radius=14, fill=c["bot_bubble"], outline="")
        canvas.create_text(45, 18, text="● ● ●", font=("Segoe UI", 10), fill=c["accent"])

        self._scroll_to_bottom()

    def _hide_typing_indicator(self):
        if hasattr(self, "typing_row") and self.typing_row.winfo_exists():
            self.typing_row.destroy()

    # -------------------- SOUND EFFECTS --------------------
    @staticmethod
    def _play_sound(kind):
        if not SOUND_AVAILABLE:
            return
        try:
            if kind == "send":
                winsound.Beep(750, 60)
            elif kind == "receive":
                winsound.Beep(550, 80)
        except Exception:
            pass  # Never let a sound failure interrupt the chat

    # -------------------- CLEAR / EXPORT --------------------
    def _clear_chat(self):
        if not self.message_log:
            return
        s = STRINGS[self.language]
        confirmed = messagebox.askyesno(s["clear_confirm_title"], s["clear_confirm_msg"])
        if confirmed:
            self.message_log = []
            for widget in self.chat_frame.winfo_children():
                widget.destroy()
            self._show_welcome_message()

    def _export_chat(self):
        s = STRINGS[self.language]
        if not self.message_log:
            messagebox.showinfo("Aria", s["export_empty"])
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text File", "*.txt")],
            initialfile=f"Aria_Chat_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        )
        if not file_path:
            return
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Aria - Chat Export ({datetime.now().strftime('%Y-%m-%d %H:%M')})\n")
                f.write("=" * 50 + "\n\n")
                for text, is_user in self.message_log:
                    speaker = "You" if is_user else BOT_NAME
                    f.write(f"{speaker}: {text}\n\n")
            messagebox.showinfo("Aria", s["export_success"])
        except Exception as e:
            messagebox.showerror("Aria", s["export_error"].format(error=e))

    # -------------------- SEND / RECEIVE --------------------
    def _send_message(self):
        user_text = self.entry.get().strip()
        if not user_text:
            return

        self.entry.delete(0, tk.END)
        self._add_bubble(user_text, is_user=True)
        self.message_log.append((user_text, True))
        self._play_sound("send")

        self._show_typing_indicator()

        thread = threading.Thread(target=self._process_response, args=(user_text,))
        thread.daemon = True
        thread.start()

    def _process_response(self, user_text):
        response = self.engine.get_response(user_text, self.language)
        self.root.after(0, self._display_response, response)

    def _display_response(self, response):
        self._hide_typing_indicator()
        self._add_bubble(response, is_user=False, animate=True)
        self.message_log.append((response, False))
        self._play_sound("receive")


# ENTRY POINT
def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
