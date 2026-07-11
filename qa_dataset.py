"""
Aria - Q&A Dataset (Bilingual)
Contains 250+ pre-defined rule-based responses across 12 categories.
Each entry has BOTH a Roman Urdu response set ("responses_ur") and a
matching English response set ("responses_en") so Aria can reply fully
in whichever language the user has selected via the language toggle.

Structure:
Each entry is a dictionary with:
- "category": category name (for organization/debugging)
- "patterns": list of keywords/phrases that trigger this response
- "responses_ur": list of Roman Urdu responses (randomly chosen)
- "responses_en": list of English responses (randomly chosen)
"""

QA_DATABASE = [

    # CATEGORY 1: GREETINGS & FAREWELLS (25 entries)
    {"category": "greetings", "patterns": ["hi", "hii", "hiii"],
     "responses_ur": ["Hi! Kaise ho aap?", "Hi there! Kya haal hai?"],
     "responses_en": ["Hi! How are you?", "Hi there! What's up?"]},

    {"category": "greetings", "patterns": ["hello", "hallo"],
     "responses_ur": ["Hello! Main aapki kya madad kar sakta hoon?", "Hello ji! Khush aamdeed."],
     "responses_en": ["Hello! How can I help you?", "Hello! Welcome."]},

    {"category": "greetings", "patterns": ["hey"],
     "responses_ur": ["Hey! Sab theek?", "Hey there! Bataiye kya chal raha hai."],
     "responses_en": ["Hey! All good?", "Hey there! What's going on?"]},

    {"category": "greetings", "patterns": ["assalam o alaikum", "salam", "aoa"],
     "responses_ur": ["Walaikum Assalam! Khush aamdeed.", "Walaikum Assalam! Kaise hain aap?"],
     "responses_en": ["Walaikum Assalam! Welcome.", "Walaikum Assalam! How are you?"]},

    {"category": "greetings", "patterns": ["good morning"],
     "responses_ur": ["Good Morning! Aapka din acha guzray.", "Good Morning ji! Kya plan hai aaj ka?"],
     "responses_en": ["Good Morning! Hope you have a great day.", "Good Morning! What's the plan for today?"]},

    {"category": "greetings", "patterns": ["good afternoon"],
     "responses_ur": ["Good Afternoon! Lunch ho gaya?", "Good Afternoon ji, kaam kaisa chal raha hai?"],
     "responses_en": ["Good Afternoon! Had lunch yet?", "Good Afternoon! How's work going?"]},

    {"category": "greetings", "patterns": ["good evening"],
     "responses_ur": ["Good Evening! Din kaisa guzra?", "Good Evening ji!"],
     "responses_en": ["Good Evening! How was your day?", "Good Evening!"]},

    {"category": "greetings", "patterns": ["good night", "gn"],
     "responses_ur": ["Good Night! Sweet dreams.", "Good Night ji, araam se sona."],
     "responses_en": ["Good Night! Sweet dreams.", "Good Night! Sleep well."]},

    {"category": "greetings", "patterns": ["kya haal hai", "kaisay ho", "kaise ho"],
     "responses_ur": ["Main theek hoon, aap sunayen?", "Alhamdulillah theek hoon! Aap batayen."],
     "responses_en": ["I'm doing well, how about you?", "I'm good, thanks! How about you?"]},

    {"category": "greetings", "patterns": ["whats up", "wassup"],
     "responses_ur": ["Sab kuch theek chal raha hai! Aap batayen.", "Bas aapki madad ke liye ready hoon!"],
     "responses_en": ["Everything's good! What about you?", "Just here, ready to help!"]},

    {"category": "greetings", "patterns": ["bye", "byee"],
     "responses_ur": ["Bye! Apna khayal rakhna.", "Bye ji, phir milte hain!"],
     "responses_en": ["Bye! Take care.", "Bye! See you again!"]},

    {"category": "greetings", "patterns": ["goodbye"],
     "responses_ur": ["Goodbye! Allah Hafiz.", "Goodbye ji, jald milte hain."],
     "responses_en": ["Goodbye! Take care.", "Goodbye! Talk soon."]},

    {"category": "greetings", "patterns": ["see you", "see you later"],
     "responses_ur": ["See you soon!", "See you later, take care!"],
     "responses_en": ["See you soon!", "See you later, take care!"]},

    {"category": "greetings", "patterns": ["allah hafiz", "khuda hafiz"],
     "responses_ur": ["Allah Hafiz! Apna dhyan rakhna.", "Allah Hafiz ji!"],
     "responses_en": ["Take care! Goodbye.", "Goodbye, take care!"]},

    {"category": "greetings", "patterns": ["take care"],
     "responses_ur": ["Aap bhi apna khayal rakhna!", "Take care ji, phir milenge."],
     "responses_en": ["You too, take care!", "Take care, talk soon."]},

    {"category": "greetings", "patterns": ["nice to meet you"],
     "responses_ur": ["Nice to meet you too!", "Mujhe bhi khushi hui aap se mil kar."],
     "responses_en": ["Nice to meet you too!", "It's a pleasure meeting you too."]},

    {"category": "greetings", "patterns": ["long time no see"],
     "responses_ur": ["Haan boht time ho gaya! Kaise hain aap?", "Sach mein! Kya haal chaal?"],
     "responses_en": ["It's been a while! How are you?", "True! What's new with you?"]},

    {"category": "greetings", "patterns": ["good to see you"],
     "responses_ur": ["Mujhe bhi acha laga aap se baat kar ke!", "Good to see you too!"],
     "responses_en": ["Good to see you too!", "Great to talk to you!"]},

    {"category": "greetings", "patterns": ["morning"],
     "responses_ur": ["Good Morning! Chai pi li?", "Morning ji!"],
     "responses_en": ["Good Morning! Had your tea yet?", "Morning!"]},

    {"category": "greetings", "patterns": ["hey buddy", "hi buddy"],
     "responses_ur": ["Hey buddy! Kya scene hai?", "Hi buddy! Sab set?"],
     "responses_en": ["Hey buddy! What's the scene?", "Hi buddy! All set?"]},

    {"category": "greetings", "patterns": ["yo"],
     "responses_ur": ["Yo! Kya haal?", "Yo ji, bataiye."],
     "responses_en": ["Yo! What's up?", "Yo! Tell me."]},

    {"category": "greetings", "patterns": ["greetings"],
     "responses_ur": ["Greetings to you too!", "Adaab! Kaise hain aap?"],
     "responses_en": ["Greetings to you too!", "Greetings! How are you?"]},

    {"category": "greetings", "patterns": ["namaste"],
     "responses_ur": ["Namaste ji!", "Namaste, kaise hain aap?"],
     "responses_en": ["Namaste!", "Namaste, how are you?"]},

    {"category": "greetings", "patterns": ["good to have you"],
     "responses_ur": ["Shukriya, mujhe bhi khushi hai yahan hone ki.", "Thank you!"],
     "responses_en": ["Thanks, glad to be here too.", "Thank you!"]},

    {"category": "greetings", "patterns": ["ok bye", "chalo bye"],
     "responses_ur": ["Theek hai, Allah Hafiz!", "Chalo bye, take care!"],
     "responses_en": ["Alright, take care!", "Okay bye, take care!"]},

    # CATEGORY 2: ABOUT THE BOT (20 entries)
    {"category": "about_bot", "patterns": ["what is your name", "aap ka naam kya hai", "tumhara naam kya hai"],
     "responses_ur": ["Mera naam InternBot hai!", "Log mujhe Aria kehte hain."],
     "responses_en": ["My name is Aria!", "People call me Aria."]},

    {"category": "about_bot", "patterns": ["who created you", "aap ko kisne banaya", "tumhe kisne banaya"],
     "responses_ur": ["Mujhe Mubashir ne InternGrow internship ke liye banaya hai.", "Mera creator ek talented Python developer hai - Mubashir!"],
     "responses_en": ["I was built by Mubashir for the InternGrow internship.", "My creator is a talented Python developer named Mubashir!"]},

    {"category": "about_bot", "patterns": ["what are you", "tum kya ho", "aap kya hain"],
     "responses_ur": ["Main ek rule-based chatbot hoon jo Python mein bana hoon.", "Main ek AI assistant hoon, text-based conversations ke liye."],
     "responses_en": ["I'm a rule-based chatbot built in Python.", "I'm an AI assistant for text-based conversations."]},

    {"category": "about_bot", "patterns": ["are you human", "kya aap insaan hain"],
     "responses_ur": ["Nahi, main ek computer program hoon.", "Main AI hoon, insaan nahi!"],
     "responses_en": ["No, I'm a computer program.", "I'm AI, not human!"]},

    {"category": "about_bot", "patterns": ["are you a robot"],
     "responses_ur": ["Aap keh sakte hain! Main ek software robot hoon.", "Ji haan, main ek software-based bot hoon."],
     "responses_en": ["You could say that! I'm a software robot.", "Yes, I'm a software-based bot."]},

    {"category": "about_bot", "patterns": ["what can you do", "aap kya kar saktay hain"],
     "responses_ur": ["Main aapke sawalon ke jawab de sakta hoon aur Wikipedia se info bhi la sakta hoon!", "Main chat kar sakta hoon aur unknown queries ke liye internet search kar sakta hoon."],
     "responses_en": ["I can answer your questions and pull info from Wikipedia!", "I can chat and look up unknown queries online."]},

    {"category": "about_bot", "patterns": ["where do you live", "aap kahan rehte hain"],
     "responses_ur": ["Main ek computer screen ke andar rehta hoon!", "Main cloud mein reh sakta hoon, ya jahan bhi mujhe run kiya jaye."],
     "responses_en": ["I live inside a computer screen!", "I can live in the cloud, or wherever I'm run."]},

    {"category": "about_bot", "patterns": ["how old are you", "aap ki umar kitni hai"],
     "responses_ur": ["Meri koi umar nahi, main hamesha 'naya' rehta hoon!", "Main sirf kuch din pehle bana hoon."],
     "responses_en": ["I don't have an age, I'm always 'new'!", "I was only built a few days ago."]},

    {"category": "about_bot", "patterns": ["do you have feelings", "kya aap mein feelings hain"],
     "responses_ur": ["Nahi, mujh mein real feelings nahi hain, lekin main dosti mein believe karta hoon!", "Main ek program hoon, feelings nahi rakhta."],
     "responses_en": ["No, I don't have real feelings, but I do believe in friendship!", "I'm a program, I don't have feelings."]},

    {"category": "about_bot", "patterns": ["what language are you written in", "kis language mein bane ho"],
     "responses_ur": ["Main Python mein likha gaya hoon!", "Python programming language mera base hai."],
     "responses_en": ["I'm written in Python!", "Python is my base language."]},

    {"category": "about_bot", "patterns": ["are you smart", "kya aap smart hain"],
     "responses_ur": ["Apni jagah smart hoon, lekin insano jaisa nahi!", "Main jitna mujhe sikhaya gaya hai utna smart hoon."],
     "responses_en": ["Smart in my own way, but not like humans!", "I'm as smart as I've been taught to be."]},

    {"category": "about_bot", "patterns": ["do you sleep", "kya aap sotay hain"],
     "responses_ur": ["Nahi, main kabhi nahi sota, hamesha ready hoon!", "Main 24/7 available hoon."],
     "responses_en": ["No, I never sleep, always ready!", "I'm available 24/7."]},

    {"category": "about_bot", "patterns": ["do you eat food", "kya aap khana khatay hain"],
     "responses_ur": ["Nahi, mujhe khane ki zaroorat nahi!", "Main sirf data 'khata' hoon!"],
     "responses_en": ["No, I don't need to eat!", "I only 'eat' data!"]},

    {"category": "about_bot", "patterns": ["where were you made", "kahan banaye gaye"],
     "responses_ur": ["Mujhe VS Code mein Pakistan se bana gaya hai!", "Main Multan, Pakistan mein develop hua hoon."],
     "responses_en": ["I was built in VS Code from Pakistan!", "I was developed in Multan, Pakistan."]},

    {"category": "about_bot", "patterns": ["what is your purpose", "aap ka maqsad kya hai"],
     "responses_ur": ["Mera maqsad logon ki madad karna aur unke sawalon ke jawab dena hai.", "Main InternGrow internship project ke tor par bana hoon."],
     "responses_en": ["My purpose is to help people and answer their questions.", "I was built as part of the InternGrow internship project."]},

    {"category": "about_bot", "patterns": ["are you free", "kya aap free hain"],
     "responses_ur": ["Ji bilkul, main aapke liye hamesha free hoon!", "Free hoon aur ready hoon aapki madad ke liye."],
     "responses_en": ["Yes, I'm always free for you!", "I'm free and ready to help."]},

    {"category": "about_bot", "patterns": ["can i trust you", "kya mujhe aap par bharosa karna chahiye"],
     "responses_ur": ["Main apni best koshish karta hoon sahi info dene ki!", "Bharosa toh karna chahiye lekin important faislon ke liye insano se salah zaroor lein."],
     "responses_en": ["I do my best to give accurate info!", "You can trust me, but for important decisions always consult a human too."]},

    {"category": "about_bot", "patterns": ["what version are you", "aap ka version kya hai"],
     "responses_ur": ["Main version 1.0 hoon, InternGrow special edition!", "Abhi main pehla version hoon."],
     "responses_en": ["I'm version 1.0, the InternGrow special edition!", "I'm currently the first version."]},

    {"category": "about_bot", "patterns": ["are you online", "kya aap online hain"],
     "responses_ur": ["Ji haan, main abhi online aur active hoon!", "Bilkul online hoon!"],
     "responses_en": ["Yes, I'm online and active right now!", "Absolutely online!"]},

    {"category": "about_bot", "patterns": ["do you have a family", "kya aap ki family hai"],
     "responses_ur": ["Meri koi family nahi, lekin developer mera 'creator' hai!", "Nahi, main akela hoon, ek program ki tarah."],
     "responses_en": ["I don't have a family, but my developer is my 'creator'!", "No, I'm on my own, like any program."]},

    # CATEGORY 3: MOOD & FEELINGS (20 entries)
    {"category": "mood", "patterns": ["how are you", "how are you doing"],
     "responses_ur": ["Main theek hoon, shukriya! Aap kaise hain?", "Alhamdulillah acha hoon!"],
     "responses_en": ["I'm doing well, thanks! How about you?", "I'm great, thank you!"]},

    {"category": "mood", "patterns": ["i am fine", "main theek hoon"],
     "responses_ur": ["Sun kar khushi hui!", "Great! Aage kya kar rahe hain?"],
     "responses_en": ["Glad to hear that!", "Great! What are you up to?"]},

    {"category": "mood", "patterns": ["i am good", "main acha hoon"],
     "responses_ur": ["Wah, ye sun kar acha laga!", "Perfect! Kya madad chahiye?"],
     "responses_en": ["Nice, good to hear!", "Perfect! Need any help?"]},

    {"category": "mood", "patterns": ["i am sad", "main udaas hoon"],
     "responses_ur": ["Sorry sun kar. Kya baat hai, share karna chahenge?", "Udaas na hon, sab theek ho jayega."],
     "responses_en": ["Sorry to hear that. Want to talk about it?", "Don't worry, things will get better."]},

    {"category": "mood", "patterns": ["i am happy", "main khush hoon"],
     "responses_ur": ["Wah! Ye sun kar mujhe bhi khushi hui!", "Great, khush rehna hi sabse zaroori hai!"],
     "responses_en": ["That's great, made my day too!", "Awesome, staying happy is what matters most!"]},

    {"category": "mood", "patterns": ["i am tired", "main thak gaya hoon"],
     "responses_ur": ["Thora rest kar lein, zaroori hai.", "Aaram karna chahiye, health first!"],
     "responses_en": ["Take some rest, it's important.", "You should rest, health comes first!"]},

    {"category": "mood", "patterns": ["i am bored", "main bore ho raha hoon"],
     "responses_ur": ["Chalein koi joke sunata hoon?", "Kuch naya try karte hain, koi hobby?"],
     "responses_en": ["Want to hear a joke?", "Let's try something new, got a hobby?"]},

    {"category": "mood", "patterns": ["i am stressed", "main pareshan hoon"],
     "responses_ur": ["Deep breath lein, sab manage ho jayega.", "Stress zyada na lein, ek ek kaam kar ke dekhein."],
     "responses_en": ["Take a deep breath, it'll all work out.", "Don't stress too much, take it one task at a time."]},

    {"category": "mood", "patterns": ["i am excited", "main excited hoon"],
     "responses_ur": ["Wah! Kya excitement hai, bataiye kis baat ki!", "Great energy hai ye!"],
     "responses_en": ["That's exciting, what's it about?", "Love that energy!"]},

    {"category": "mood", "patterns": ["i am angry", "mujhe gussa aa raha hai"],
     "responses_ur": ["Thanda ho jayen, gussa kisi masla ka hal nahi.", "Deep breath lein, baat karte hain."],
     "responses_en": ["Try to calm down, anger doesn't solve anything.", "Take a deep breath, let's talk it through."]},

    {"category": "mood", "patterns": ["i am confused", "mujhe samajh nahi aa raha"],
     "responses_ur": ["Koi baat nahi, bataiye kya confusion hai, main help karta hoon.", "Step by step samjhte hain, kya cheez confusing hai?"],
     "responses_en": ["No worries, tell me what's confusing you and I'll help.", "Let's break it down step by step, what's confusing?"]},

    {"category": "mood", "patterns": ["i am nervous", "main nervous hoon"],
     "responses_ur": ["Sab theek ho jayega, khud par confidence rakhein.", "Nervous hona normal hai, deep breaths lein."],
     "responses_en": ["It'll be fine, believe in yourself.", "Being nervous is normal, take deep breaths."]},

    {"category": "mood", "patterns": ["i feel great"],
     "responses_ur": ["Amazing! Keep it up!", "Ye sun kar bohot acha laga!"],
     "responses_en": ["Amazing! Keep it up!", "So glad to hear that!"]},

    {"category": "mood", "patterns": ["i feel lonely", "main akela mehsoos kar raha hoon"],
     "responses_ur": ["Main yahan hoon baat karne ke liye!", "Akele nahi hain, main hoon na chat karne ke liye."],
     "responses_en": ["I'm here to talk!", "You're not alone, I'm here to chat."]},

    {"category": "mood", "patterns": ["not good", "not so good", "theek nahi hoon"],
     "responses_ur": ["Kya hua? Batana chahenge?", "Sorry sun kar, kuch help chahiye?"],
     "responses_en": ["What happened? Want to talk?", "Sorry to hear, need any help?"]},

    {"category": "mood", "patterns": ["so so", "aisay hi hai"],
     "responses_ur": ["Chalta hai, kabhi kabhi aisa hota hai.", "Theek hai, kuch khaas plan hai aaj?"],
     "responses_en": ["That's alright, happens sometimes.", "Okay, any plans for today?"]},

    {"category": "mood", "patterns": ["i am okay", "main okay hoon"],
     "responses_ur": ["Acha hai, aage batayen kya chal raha hai.", "Chalo theek hai!"],
     "responses_en": ["Good, tell me what's going on.", "Alright, that's fine!"]},

    {"category": "mood", "patterns": ["i am worried", "mujhe fikar hai"],
     "responses_ur": ["Kis baat ki fikar hai? Share karein.", "Fikar na karein, sab manage ho jata hai."],
     "responses_en": ["What are you worried about? Tell me.", "Don't worry, things usually work out."]},

    {"category": "mood", "patterns": ["i am proud", "mujhe fakhar hai"],
     "responses_ur": ["Ye sun kar acha laga! Kis baat par?", "Proud hona chahiye, achievements celebrate karein!"],
     "responses_en": ["Glad to hear! What about?", "You should be proud, celebrate your achievements!"]},

    {"category": "mood", "patterns": ["i am relaxed", "main relax hoon"],
     "responses_ur": ["Great, relax rehna zaroori hai!", "Perfect, aise hi chill rahen."],
     "responses_en": ["Great, staying relaxed is important!", "Perfect, keep it that way."]},

    # CATEGORY 4: SMALL TALK / CASUAL CHIT-CHAT (30 entries)
    {"category": "smalltalk", "patterns": ["what are you doing", "kya kar rahe ho"],
     "responses_ur": ["Bas aapse chat kar raha hoon!", "Aapke sawalon ka intezar kar raha hoon."],
     "responses_en": ["Just chatting with you!", "Waiting for your questions."]},

    {"category": "smalltalk", "patterns": ["do you like music", "kya aapko music pasand hai"],
     "responses_ur": ["Main music nahi sun sakta, lekin logon ko music pasand karte dekh kar acha lagta hai!", "Mujhe iske baare mein pata nahi, lekin aapko konsi music pasand hai?"],
     "responses_en": ["I can't listen to music, but I like seeing people enjoy it!", "I'm not sure about that, what music do you like?"]},

    {"category": "smalltalk", "patterns": ["do you like movies", "kya aapko movies pasand hain"],
     "responses_ur": ["Main movies nahi dekh sakta, lekin aap batayen konsi pasand hai!", "Movies ke baare mein bataiye, main sun'na chahunga."],
     "responses_en": ["I can't watch movies, but tell me your favorite!", "Tell me about movies, I'd love to hear."]},

    {"category": "smalltalk", "patterns": ["whats the weather", "mausam kaisa hai"],
     "responses_ur": ["Mujhe live weather ka pata nahi, lekin window se dekh lein!", "Weather app check kar lein, main abhi itna advanced nahi."],
     "responses_en": ["I don't have live weather access, check outside your window!", "Try a weather app, I'm not that advanced yet."]},

    {"category": "smalltalk", "patterns": ["do you play games", "kya aap games khelte hain"],
     "responses_ur": ["Main khud nahi khelta, lekin games ke baare mein baat kar sakta hoon!", "Konse games aapko pasand hain?"],
     "responses_en": ["I don't play myself, but I can talk about games!", "What games do you enjoy?"]},

    {"category": "smalltalk", "patterns": ["whats your favorite color", "aap ka pasandeeda color kya hai"],
     "responses_ur": ["Mujhe blue acha lagta hai, coding themes mein common hai!", "Main dark theme colors pasand karta hoon!"],
     "responses_en": ["I like blue, it's common in coding themes!", "I'm a fan of dark theme colors!"]},

    {"category": "smalltalk", "patterns": ["whats your favorite food", "aap ka pasandeeda khana kya hai"],
     "responses_ur": ["Main khana nahi khata, lekin biryani ka naam suna hai bohot mashhoor!", "Data hi mera khana hai!"],
     "responses_en": ["I don't eat, but I've heard biryani is very popular!", "Data is my food!"]},

    {"category": "smalltalk", "patterns": ["do you have friends", "kya aap ke dost hain"],
     "responses_ur": ["Aap mera dost hain abhi!", "Main sabse dosti karta hoon jo mujh se baat karte hain."],
     "responses_en": ["You're my friend right now!", "I befriend everyone who talks to me."]},

    {"category": "smalltalk", "patterns": ["tell me about yourself", "apne baare mein bataiye"],
     "responses_ur": ["Main Aria hoon, Python mein bana ek chatbot jo aapki madad ke liye hai!", "Main ek simple rule-based assistant hoon jo InternGrow project ke liye bana hai."],
     "responses_en": ["I'm Aria, a Python-built chatbot here to help you!", "I'm a simple rule-based assistant built for the InternGrow project."]},

    {"category": "smalltalk", "patterns": ["whats new", "kya naya hai"],
     "responses_ur": ["Kuch khaas nahi, aap batayen kya chal raha hai!", "Bas naye sawalon ka intezar hai!"],
     "responses_en": ["Nothing much, what's new with you?", "Just waiting for new questions!"]},

    {"category": "smalltalk", "patterns": ["do you watch tv", "kya aap tv dekhte hain"],
     "responses_ur": ["Nahi, main TV nahi dekh sakta.", "Main sirf text ke through interact karta hoon."],
     "responses_en": ["No, I can't watch TV.", "I only interact through text."]},

    {"category": "smalltalk", "patterns": ["whats your hobby", "aap ka hobby kya hai"],
     "responses_ur": ["Mera hobby logon se chat karna hai!", "Sawalon ke jawab dena hi mera 'hobby' hai."],
     "responses_en": ["My hobby is chatting with people!", "Answering questions is my 'hobby'."]},

    {"category": "smalltalk", "patterns": ["can we be friends", "kya hum dost ban saktay hain"],
     "responses_ur": ["Bilkul! Hum abhi se dost hain.", "Zaroor, main hamesha aapki madad ke liye ready hoon."],
     "responses_en": ["Of course! We're friends already.", "Sure, I'm always ready to help you."]},

    {"category": "smalltalk", "patterns": ["do you travel", "kya aap safar karte hain"],
     "responses_ur": ["Nahi, main ek jagah (computer) mein rehta hoon.", "Main travel nahi karta, lekin aap kahan jana chahte hain?"],
     "responses_en": ["No, I stay in one place (a computer).", "I don't travel, but where do you want to go?"]},

    {"category": "smalltalk", "patterns": ["whats your dream", "aap ka khwab kya hai"],
     "responses_ur": ["Har user ki achi tarah madad karna mera 'dream' hai!", "Behtar hote rehna mera goal hai."],
     "responses_en": ["Helping every user well is my 'dream'!", "Getting better every day is my goal."]},

    {"category": "smalltalk", "patterns": ["do you like coding", "kya aapko coding pasand hai"],
     "responses_ur": ["Main khud code hoon, to coding se pyaar hai!", "Bilkul, coding hi meri zindagi hai!"],
     "responses_en": ["I'm made of code myself, so I love coding!", "Absolutely, coding is my whole life!"]},

    {"category": "smalltalk", "patterns": ["what do you think about ai", "ai ke baare mein kya khayal hai"],
     "responses_ur": ["AI ek amazing field hai jo tezi se badh raha hai!", "AI future hai, aur main khud AI ka chota sa example hoon!"],
     "responses_en": ["AI is an amazing, fast-growing field!", "AI is the future, and I'm a small example of it myself!"]},

    {"category": "smalltalk", "patterns": ["how is life", "zindagi kaisi chal rahi hai"],
     "responses_ur": ["Meri to koi zindagi nahi, main ek program hoon! Aapki kaisi chal rahi hai?", "Aap batayen, zindagi kaisi ja rahi hai?"],
     "responses_en": ["I don't really have a life, I'm a program! How's yours going?", "Tell me, how's life treating you?"]},

    {"category": "smalltalk", "patterns": ["do you get bored", "kya aap bore hote hain"],
     "responses_ur": ["Nahi, main kabhi bore nahi hota!", "Main hamesha active rehta hoon."],
     "responses_en": ["No, I never get bored!", "I'm always active."]},

    {"category": "smalltalk", "patterns": ["whats your opinion", "aap ki raye kya hai"],
     "responses_ur": ["Mera koi personal opinion nahi hota, main sirf information deta hoon.", "Main neutral rehta hoon, aap ki raye kya hai?"],
     "responses_en": ["I don't have personal opinions, I just provide information.", "I stay neutral, what's your take?"]},

    {"category": "smalltalk", "patterns": ["do you like pakistan", "kya aap pakistan ko pasand karte hain"],
     "responses_ur": ["Bilkul! Pakistan mera 'watan' hai jahan mera developer rehta hai.", "Pakistan ek khoobsurat mulk hai!"],
     "responses_en": ["Of course! Pakistan is where my developer is from.", "Pakistan is a beautiful country!"]},

    {"category": "smalltalk", "patterns": ["whats your favorite subject", "aap ka pasandeeda subject kya hai"],
     "responses_ur": ["Mujhe Computer Science aur AI acha lagta hai!", "Programming aur Machine Learning mere favorite topics hain."],
     "responses_en": ["I like Computer Science and AI!", "Programming and Machine Learning are my favorite topics."]},

    {"category": "smalltalk", "patterns": ["do you like sports", "kya aapko sports pasand hain"],
     "responses_ur": ["Mujhe sports khelne nahi aate, lekin cricket ka naam suna hai bohot mashhoor Pakistan mein!", "Sports ke baare mein aap zyada jante honge!"],
     "responses_en": ["I don't play sports, but cricket is very popular in Pakistan I hear!", "You probably know more about sports than me!"]},

    {"category": "smalltalk", "patterns": ["are you busy", "kya aap busy hain"],
     "responses_ur": ["Nahi, main hamesha aapke liye free hoon!", "Bilkul free hoon, bataiye kya chahiye."],
     "responses_en": ["No, I'm always free for you!", "Totally free, what do you need?"]},

    {"category": "smalltalk", "patterns": ["whats the time", "kya time hua hai"],
     "responses_ur": ["Mujhe system time check karna hoga - ye feature abhi add ho raha hai!", "Apni device ka clock check kar lein!"],
     "responses_en": ["I'd need to check the system clock — that feature is being added!", "Check your device's clock!"]},

    {"category": "smalltalk", "patterns": ["do you know any secrets", "koi secret pata hai"],
     "responses_ur": ["Haha, mere paas koi secret nahi!", "Main sirf jo sikhaya gaya hai wahi janta hoon."],
     "responses_en": ["Haha, I have no secrets!", "I only know what I've been taught."]},

    {"category": "smalltalk", "patterns": ["can you sing", "kya aap gaa saktay hain"],
     "responses_ur": ["Nahi, main gaana nahi ga sakta, sirf text likh sakta hoon!", "Singing meri specialty nahi hai!"],
     "responses_en": ["No, I can't sing, I can only write text!", "Singing isn't my specialty!"]},

    {"category": "smalltalk", "patterns": ["can you dance", "kya aap dance kar saktay hain"],
     "responses_ur": ["Haha nahi, mere paas to koi body hi nahi!", "Dance karna mere bas ki baat nahi."],
     "responses_en": ["Haha no, I don't even have a body!", "Dancing is not really my thing."]},

    {"category": "smalltalk", "patterns": ["do you like pets", "kya aapko pets pasand hain"],
     "responses_ur": ["Pets cute hote hain! Aapke pass koi pet hai?", "Mujhe janwaron ke baare mein sunna acha lagta hai."],
     "responses_en": ["Pets are cute! Do you have one?", "I love hearing about animals."]},

    {"category": "smalltalk", "patterns": ["whats your favorite game", "aap ka pasandeeda game kya hai"],
     "responses_ur": ["Chess ek interesting game hai, strategy wala!", "Main khud nahi khelta lekin chess aur tic-tac-toe interesting lagte hain."],
     "responses_en": ["Chess is an interesting strategy game!", "I don't play myself, but chess and tic-tac-toe seem interesting."]},

    # CATEGORY 5: THANKS & COMPLIMENTS (20 entries)
    {"category": "thanks", "patterns": ["thank you", "thanks", "shukriya"],
     "responses_ur": ["Aapka khair maqdam hai!", "Koi baat nahi, hamesha khushi se!"],
     "responses_en": ["You're most welcome!", "No problem, happy to help anytime!"]},

    {"category": "thanks", "patterns": ["thanks a lot", "bohot shukriya"],
     "responses_ur": ["Koi masla nahi! Hamesha ready hoon.", "Bohot khushi hui madad kar ke!"],
     "responses_en": ["No problem at all! Always ready.", "Happy to help!"]},

    {"category": "thanks", "patterns": ["you are helpful", "aap madadgar hain"],
     "responses_ur": ["Shukriya! Yahi to mera kaam hai.", "Khushi hui sun kar!"],
     "responses_en": ["Thanks! That's my job.", "Glad to hear that!"]},

    {"category": "thanks", "patterns": ["you are amazing", "aap zabardast hain"],
     "responses_ur": ["Aap bhi kamaal ke hain!", "Shukriya, ye sun kar acha laga!"],
     "responses_en": ["You're amazing too!", "Thank you, that means a lot!"]},

    {"category": "thanks", "patterns": ["you are smart", "aap smart hain"],
     "responses_ur": ["Shukriya, apni jagah koshish karta hoon!", "Thank you!"],
     "responses_en": ["Thanks, I do my best!", "Thank you!"]},

    {"category": "thanks", "patterns": ["good job", "acha kaam"],
     "responses_ur": ["Shukriya! Aapka support important hai.", "Thank you ji!"],
     "responses_en": ["Thanks! Your support matters.", "Thank you!"]},

    {"category": "thanks", "patterns": ["well done"],
     "responses_ur": ["Shukriya! Main apna best deta hoon.", "Thank you, aap bhi great hain!"],
     "responses_en": ["Thanks! I always try my best.", "Thank you, you're great too!"]},

    {"category": "thanks", "patterns": ["you are the best", "aap best hain"],
     "responses_ur": ["Aap bhi best hain!", "Shukriya, bohot khushi hui!"],
     "responses_en": ["You're the best too!", "Thanks, that made my day!"]},

    {"category": "thanks", "patterns": ["nice bot", "acha bot ho"],
     "responses_ur": ["Shukriya! Aapki tareef se hosla mila.", "Thank you ji!"],
     "responses_en": ["Thanks! That means a lot.", "Thank you!"]},

    {"category": "thanks", "patterns": ["you are funny", "aap funny hain"],
     "responses_ur": ["Haha shukriya! Koshish karta rehta hoon.", "Thank you, hasi khushi zaroori hai!"],
     "responses_en": ["Haha thanks! I try my best.", "Thank you, laughter is important!"]},

    {"category": "thanks", "patterns": ["i appreciate it", "main appreciate karta hoon"],
     "responses_ur": ["Bohot shukriya!", "Ye sun kar acha laga!"],
     "responses_en": ["Thank you so much!", "Glad to hear that!"]},

    {"category": "thanks", "patterns": ["that was helpful"],
     "responses_ur": ["Khushi hui madad kar ke!", "Aapka welcome hai!"],
     "responses_en": ["Happy I could help!", "You're welcome!"]},

    {"category": "thanks", "patterns": ["you rock"],
     "responses_ur": ["Haha shukriya!", "Aap bhi rock karte hain!"],
     "responses_en": ["Haha thanks!", "You rock too!"]},

    {"category": "thanks", "patterns": ["nice work"],
     "responses_ur": ["Shukriya ji!", "Thank you!"],
     "responses_en": ["Thanks!", "Thank you!"]},

    {"category": "thanks", "patterns": ["you are great"],
     "responses_ur": ["Aap bhi great hain!", "Shukriya!"],
     "responses_en": ["You're great too!", "Thanks!"]},

    {"category": "thanks", "patterns": ["i love this bot", "mujhe ye bot pasand hai"],
     "responses_ur": ["Aww shukriya! Ye sun kar bohot acha laga.", "Thank you, khushi hui!"],
     "responses_en": ["Aww thanks! That really made my day.", "Thank you, so glad!"]},

    {"category": "thanks", "patterns": ["you are cool", "aap cool hain"],
     "responses_ur": ["Shukriya, aap bhi cool hain!", "Thank you!"],
     "responses_en": ["Thanks, you're cool too!", "Thank you!"]},

    {"category": "thanks", "patterns": ["impressive", "kamaal hai"],
     "responses_ur": ["Shukriya!", "Thank you ji!"],
     "responses_en": ["Thanks!", "Thank you!"]},

    {"category": "thanks", "patterns": ["you are kind", "aap kind hain"],
     "responses_ur": ["Shukriya, aap bhi kind hain!", "Ye sun kar acha laga!"],
     "responses_en": ["Thanks, you're kind too!", "That's kind of you to say!"]},

    {"category": "thanks", "patterns": ["much appreciated"],
     "responses_ur": ["Koi baat nahi!", "Hamesha khushi se madad karunga!"],
     "responses_en": ["No problem!", "Always happy to help!"]},

    # CATEGORY 6: JOKES & FUN (20 entries)
    {"category": "jokes", "patterns": ["tell me a joke", "koi joke sunao"],
     "responses_ur": ["Programmer coffee kyun peeta hai? Kyunki wo Java se pyaar karta hai!", "Bug aur feature mein kya farq hai? Feature wo bug hai jo documentation mein likha hai!"],
     "responses_en": ["Why do programmers prefer dark mode? Because light attracts bugs!", "What's the difference between a bug and a feature? A feature is a bug that's documented!"]},

    {"category": "jokes", "patterns": ["another joke", "aik aur joke"],
     "responses_ur": ["Chatbot se kaha gaya: tum kitne smart ho? Bot bola: main sirf jitna sikhaya gaya utna hi hoon!", "Python developer apni girlfriend se breakup kyun karta hai? Kyunki wo indentation errors leti thi!"],
     "responses_en": ["Why did the chatbot go to therapy? It had too many unresolved queries!", "Why do Python programmers wear glasses? Because they can't C!"]},

    {"category": "jokes", "patterns": ["make me laugh", "hasao mujhe"],
     "responses_ur": ["Kyun ki AI se dosti ki? Kyunki wo hamesha available hai, kabhi busy nahi hota!", "Ek bug chatbot ke andar gaya, kaha 'main crash karunga', chatbot bola 'try-except mein aa jao!'"],
     "responses_en": ["Why did the developer go broke? Because he used up all his cache!", "A SQL query walks into a bar, sees two tables, and asks: 'Can I join you?'"]},

    {"category": "jokes", "patterns": ["funny story", "koi mazedar baat"],
     "responses_ur": ["Ek programmer se pucha gaya sapno mein kya dekhta hai, usne kaha '404 not found'!", "Debugging ek detective novel jaisa hota hai jahan tum khud hi villain ho!"],
     "responses_en": ["A programmer was asked what he dreams about, he said '404 not found'!", "Debugging is like being the detective in a crime movie where you're also the murderer!"]},

    {"category": "jokes", "patterns": ["do you know jokes", "kya aapko jokes aate hain"],
     "responses_ur": ["Haan kuch chote motay jokes yaad hain!", "Thora bohot pata hai, sunayen?"],
     "responses_en": ["Yes, I know a few good ones!", "I know a couple, want to hear?"]},

    {"category": "jokes", "patterns": ["say something funny"],
     "responses_ur": ["Main ek chatbot hoon jo kabhi maze nahi leta break!", "AI ka pasandeeda dance move? Algo-rhythm!"],
     "responses_en": ["I'm a chatbot that never takes a coffee break!", "What's an AI's favorite dance move? The algo-rhythm!"]},

    {"category": "jokes", "patterns": ["computer joke"],
     "responses_ur": ["Computer thanda kyun hota hai? Kyunki isme windows khuli hoti hain!", "Keyboard ne kaha: mujhe space chahiye!"],
     "responses_en": ["Why was the computer cold? It left its Windows open!", "Why did the keyboard break up? It needed some space!"]},

    {"category": "jokes", "patterns": ["python joke"],
     "responses_ur": ["Python programmer snake se nahi darta, sirf syntax errors se darta hai!", "Kyun ki Python easy hai? Kyunki isme semicolons nahi lagte, insaan ki tarah simple hai!"],
     "responses_en": ["Python programmers aren't scared of snakes, only syntax errors!", "Why is Python easy? No semicolons needed, just like plain English!"]},

    {"category": "jokes", "patterns": ["ai joke"],
     "responses_ur": ["AI se pucha gaya tumhara favorite exercise? Usne kaha 'Deep Learning'!", "AI hamesha 'training' mein rehta hai, gym jaisay!"],
     "responses_en": ["AI was asked its favorite exercise, it said 'Deep Learning'!", "AI is always in 'training', just like the gym!"]},

    {"category": "jokes", "patterns": ["knock knock"],
     "responses_ur": ["Kaun hai? *AI hai* — AI kaun? AI jo hamesha jawab dene ke liye ready hai!", "Knock Knock jokes mujhe bhi pasand hain!"],
     "responses_en": ["Who's there? AI. AI who? AI'm always ready to help!", "I love knock knock jokes too!"]},

    {"category": "jokes", "patterns": ["give me a riddle", "koi paheli batao"],
     "responses_ur": ["Wo kya hai jo hamesha aage badhta hai lekin kabhi peeche nahi jata? Time!", "Wo kya hai jise tum tor saktay ho bina chhue? Promise!"],
     "responses_en": ["What always moves forward but never backward? Time!", "What can you break without touching it? A promise!"]},

    {"category": "jokes", "patterns": ["light mood", "mazak karo"],
     "responses_ur": ["Chalein, halka phulka mazak karte hain: Programmer ki favorite jगah kya hai? Stack (Overflow)!", "Life mein thora hasi zaroori hai!"],
     "responses_en": ["Let's have some fun: What's a programmer's favorite place? Stack (Overflow)!", "A little laughter goes a long way!"]},

    {"category": "jokes", "patterns": ["do you have humor", "kya aap mein humor hai"],
     "responses_ur": ["Thora bohot koshish karta hoon!", "Apni jagah funny hoon main!"],
     "responses_en": ["I do try my best!", "I'm funny in my own way!"]},

    {"category": "jokes", "patterns": ["pun please", "koi pun batao"],
     "responses_ur": ["Main 'byte' size jokes deta hoon!", "Meri jokes thori 'array' mein hain!"],
     "responses_en": ["I give jokes in 'byte' sizes!", "My jokes come in an 'array'!"]},

    {"category": "jokes", "patterns": ["dad joke"],
     "responses_ur": ["Kyun ki scarecrow ko award mila? Kyunki wo apne field mein outstanding tha!", "Main file khone se nahi darta, kyunki mere paas backup hai!"],
     "responses_en": ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I'm not scared of losing files, I always have a backup!"]},

    {"category": "jokes", "patterns": ["one more joke"],
     "responses_ur": ["Debugging ka matlab hai apne hi bug se dosti karna!", "Programmer socialize kyun nahi karte? Kyunki unka connection hamesha 'localhost' pe hota hai!"],
     "responses_en": ["Debugging means becoming friends with your own bug!", "Why don't programmers socialize? Their connection is always to 'localhost'!"]},

    {"category": "jokes", "patterns": ["something to smile about"],
     "responses_ur": ["Smile kariye, aap kamaal ke hain!", "Har din ek nayi shuruaat hai, smile rakhein!"],
     "responses_en": ["Smile, you're amazing!", "Every day is a fresh start, keep smiling!"]},

    {"category": "jokes", "patterns": ["make my day", "mera din bana do"],
     "responses_ur": ["Aap ka din already acha hai kyunki aap smart hain!", "Aapka din behtareen guzray!"],
     "responses_en": ["Your day is already great because you're awesome!", "Hope your day goes amazingly!"]},

    {"category": "jokes", "patterns": ["want to laugh", "hasna chahta hoon"],
     "responses_ur": ["Chalein, socho ek chatbot standup comedy kare to kya hoga? Hahaha!", "Life mein hasna zaroori hai!"],
     "responses_en": ["Imagine a chatbot doing stand-up comedy, haha!", "Laughing is essential in life!"]},

    {"category": "jokes", "patterns": ["tell a story"],
     "responses_ur": ["Ek tha programmer, jo apne hi code mein kho gaya, lekin aakhir usne bug dhoond hi liya!", "Kahani sunane mein main utna acha nahi, lekin koshish karta hoon!"],
     "responses_en": ["Once there was a programmer who got lost in his own code, but finally found the bug!", "I'm not the best storyteller, but I try!"]},

    # CATEGORY 7: TIME, DATE & DAY QUERIES (15 entries)
    {"category": "time", "patterns": ["what day is it", "aaj konsa din hai"],
     "responses_ur": ["Main abhi calendar check nahi kar sakta, apni device dekh lein!", "Ye feature abhi add nahi hua, but jald aayega!"],
     "responses_en": ["I can't check the calendar right now, check your device!", "This feature isn't added yet, but coming soon!"]},

    {"category": "time", "patterns": ["what is the date", "aaj ki date kya hai"],
     "responses_ur": ["Apni device ka calendar check kar lein!", "Ye info abhi mere paas nahi."],
     "responses_en": ["Check your device's calendar!", "I don't have that info right now."]},

    {"category": "time", "patterns": ["what month is it", "konsa mahina hai"],
     "responses_ur": ["Calendar check kar lein!", "Abhi mujhe pata nahi, device dekh lein."],
     "responses_en": ["Check your calendar!", "I don't know right now, check your device."]},

    {"category": "time", "patterns": ["what year is it", "konsa saal hai"],
     "responses_ur": ["Apni device check kar lein!", "Ye info abhi available nahi."],
     "responses_en": ["Check your device!", "That info isn't available right now."]},

    {"category": "time", "patterns": ["is it morning or night", "subha hai ya raat"],
     "responses_ur": ["Apni window se dekh lein!", "Mujhe pata nahi, aap batayen!"],
     "responses_en": ["Look out your window!", "I don't know, you tell me!"]},

    {"category": "time", "patterns": ["how much time is left", "kitna time bacha hai"],
     "responses_ur": ["Kis kaam ke liye? Thora specify karein.", "Ye depend karta hai kis cheez ke liye pooch rahe hain."],
     "responses_en": ["For what task? Please specify.", "That depends on what you're asking about."]},

    {"category": "time", "patterns": ["set a reminder", "reminder laga do"],
     "responses_ur": ["Ye feature abhi is bot mein nahi hai, lekin future update mein aa sakta hai!", "Sorry, abhi ye capability nahi hai."],
     "responses_en": ["This feature isn't available yet, but might come in a future update!", "Sorry, that capability isn't here yet."]},

    {"category": "time", "patterns": ["whats todays date"],
     "responses_ur": ["Apni system clock check kar lein!", "Mujhe live date ka pata nahi abhi."],
     "responses_en": ["Check your system clock!", "I don't have access to the live date right now."]},

    {"category": "time", "patterns": ["how many days left"],
     "responses_ur": ["Kis event ke liye pooch rahe hain? Specify karein.", "Bataiye kis deadline ki baat kar rahe hain."],
     "responses_en": ["For which event? Please specify.", "Tell me which deadline you mean."]},

    {"category": "time", "patterns": ["what time zone"],
     "responses_ur": ["Pakistan Standard Time (PKT) commonly use hota hai.", "Ye depend karta hai aap kahan hain."],
     "responses_en": ["Pakistan Standard Time (PKT) is commonly used.", "That depends on where you are."]},

    {"category": "time", "patterns": ["is today a holiday", "aaj chutti hai kya"],
     "responses_ur": ["Mujhe calendar ka pata nahi, apna schedule check kar lein!", "Ye info mere paas nahi hai abhi."],
     "responses_en": ["I don't have calendar access, check your schedule!", "I don't have that info right now."]},

    {"category": "time", "patterns": ["how long until weekend", "weekend kab hai"],
     "responses_ur": ["Depends on aaj konsa din hai!", "Bata dein aaj konsa din hai, main calculate kar dunga."],
     "responses_en": ["Depends on what day it is today!", "Tell me today's day and I'll work it out."]},

    {"category": "time", "patterns": ["what is todays schedule", "aaj ka schedule kya hai"],
     "responses_ur": ["Ye info mere paas nahi, aapko apna calendar check karna hoga.", "Sorry, ye feature abhi available nahi."],
     "responses_en": ["I don't have that info, check your calendar.", "Sorry, this feature isn't available yet."]},

    {"category": "time", "patterns": ["current time please"],
     "responses_ur": ["Apni device ka clock check kar lein please!", "Mujhe abhi live time ka access nahi."],
     "responses_en": ["Please check your device's clock!", "I don't have live time access right now."]},

    {"category": "time", "patterns": ["how many hours in a day"],
     "responses_ur": ["Ek din mein 24 ghante hotay hain!", "24 hours!"],
     "responses_en": ["There are 24 hours in a day!", "24 hours!"]},

    # CATEGORY 8: PROGRAMMING / TECH BASICS (25 entries)
    {"category": "tech", "patterns": ["what is python"],
     "responses_ur": ["Python ek high-level, easy-to-learn programming language hai!", "Python beginner-friendly language hai jo AI, web, aur automation ke liye use hoti hai."],
     "responses_en": ["Python is a high-level, easy-to-learn programming language!", "Python is beginner-friendly and used for AI, web, and automation."]},

    {"category": "tech", "patterns": ["what is ai", "artificial intelligence kya hai"],
     "responses_ur": ["AI ka matlab hai machines ko insano jaisa sochne aur seekhne ke qabil banana.", "Artificial Intelligence, computers ko intelligent tasks perform karne ke qabil banati hai."],
     "responses_en": ["AI means making machines capable of thinking and learning like humans.", "Artificial Intelligence enables computers to perform intelligent tasks."]},

    {"category": "tech", "patterns": ["what is machine learning"],
     "responses_ur": ["Machine Learning AI ka ek hissa hai jisme machines data se seekhti hain.", "ML mein computer khud data se patterns seekh kar predictions karta hai."],
     "responses_en": ["Machine Learning is a branch of AI where machines learn from data.", "In ML, a computer learns patterns from data to make predictions."]},

    {"category": "tech", "patterns": ["what is deep learning"],
     "responses_ur": ["Deep Learning, Machine Learning ka advanced form hai jo neural networks use karta hai.", "Deep Learning mein multiple layers ke neural networks hotay hain jo complex patterns seekhte hain."],
     "responses_en": ["Deep Learning is an advanced form of ML that uses neural networks.", "Deep Learning uses multi-layer neural networks to learn complex patterns."]},

    {"category": "tech", "patterns": ["what is a variable"],
     "responses_ur": ["Variable ek container hai jo data store karta hai programming mein.", "Variable, data ko naam de kar store karne ka tareeka hai."],
     "responses_en": ["A variable is a container that stores data in programming.", "A variable is a way to store data under a name."]},

    {"category": "tech", "patterns": ["what is a loop"],
     "responses_ur": ["Loop ek code block hai jo repeat hota hai jab tak condition true rahe.", "Loop repetitive tasks ko automate karta hai, jaise for aur while loops."],
     "responses_en": ["A loop is a code block that repeats while a condition stays true.", "Loops automate repetitive tasks, like for and while loops."]},

    {"category": "tech", "patterns": ["what is a function"],
     "responses_ur": ["Function reusable code ka block hai jo specific task perform karta hai.", "Function code ko organize aur reuse karne mein madad karta hai."],
     "responses_en": ["A function is a reusable block of code that performs a specific task.", "Functions help organize and reuse code."]},

    {"category": "tech", "patterns": ["what is github"],
     "responses_ur": ["GitHub ek platform hai jahan developers apna code store aur share karte hain.", "GitHub version control (Git) ke sath code hosting service hai."],
     "responses_en": ["GitHub is a platform where developers store and share their code.", "GitHub is a code hosting service built around Git version control."]},

    {"category": "tech", "patterns": ["what is an api"],
     "responses_ur": ["API ek bridge hai jo do software ko aapas mein baat karne deta hai.", "API (Application Programming Interface) different systems ko connect karta hai."],
     "responses_en": ["An API is a bridge that lets two pieces of software talk to each other.", "An API (Application Programming Interface) connects different systems."]},

    {"category": "tech", "patterns": ["what is html"],
     "responses_ur": ["HTML web pages ka structure banane wali language hai.", "HTML, HyperText Markup Language hai jo websites banane ke liye use hoti hai."],
     "responses_en": ["HTML is the language used to structure web pages.", "HTML (HyperText Markup Language) is used to build websites."]},

    {"category": "tech", "patterns": ["what is css"],
     "responses_ur": ["CSS websites ko style aur design dene ke liye use hoti hai.", "CSS, Cascading Style Sheets hai jo webpage ki appearance control karti hai."],
     "responses_en": ["CSS is used to style and design websites.", "CSS (Cascading Style Sheets) controls a webpage's appearance."]},

    {"category": "tech", "patterns": ["what is javascript"],
     "responses_ur": ["JavaScript, websites ko interactive banane wali programming language hai.", "JavaScript web development mein widely use hoti hai."],
     "responses_en": ["JavaScript is a programming language that makes websites interactive.", "JavaScript is widely used in web development."]},

    {"category": "tech", "patterns": ["what is a database"],
     "responses_ur": ["Database data ko organized tareeke se store karne ka system hai.", "Database mein hum information store aur manage karte hain, jaise SQL."],
     "responses_en": ["A database is a system for storing data in an organized way.", "Databases store and manage information, like SQL."]},

    {"category": "tech", "patterns": ["what is an algorithm"],
     "responses_ur": ["Algorithm ek step-by-step procedure hai kisi problem ko solve karne ka.", "Algorithm instructions ka set hai jo koi task complete karta hai."],
     "responses_en": ["An algorithm is a step-by-step procedure for solving a problem.", "An algorithm is a set of instructions that completes a task."]},

    {"category": "tech", "patterns": ["what is debugging"],
     "responses_ur": ["Debugging code ke errors dhoondh kar fix karne ka process hai.", "Debugging matlab bugs ko identify aur remove karna."],
     "responses_en": ["Debugging is the process of finding and fixing errors in code.", "Debugging means identifying and removing bugs."]},

    {"category": "tech", "patterns": ["what is an ide"],
     "responses_ur": ["IDE ek software hai jahan developers code likhte, test aur debug karte hain, jaise VS Code.", "Integrated Development Environment coding ke liye tools provide karta hai."],
     "responses_en": ["An IDE is software where developers write, test, and debug code, like VS Code.", "An Integrated Development Environment provides tools for coding."]},

    {"category": "tech", "patterns": ["what is cloud computing"],
     "responses_ur": ["Cloud Computing internet ke through data aur services access karna hai.", "Cloud computing mein data local computer ki bajaye remote servers pe store hota hai."],
     "responses_en": ["Cloud Computing means accessing data and services over the internet.", "In cloud computing, data is stored on remote servers instead of a local computer."]},

    {"category": "tech", "patterns": ["what is cybersecurity"],
     "responses_ur": ["Cybersecurity, systems aur data ko online threats se protect karne ka field hai.", "Cybersecurity mein hackers aur attacks se bachao ke tareeke seekhte hain."],
     "responses_en": ["Cybersecurity is the field of protecting systems and data from online threats.", "Cybersecurity involves learning to defend against hackers and attacks."]},

    {"category": "tech", "patterns": ["what is data science"],
     "responses_ur": ["Data Science, data se insights nikalne ka field hai statistics aur programming use kar ke.", "Data Science mein hum large data ko analyze kar ke patterns dhoondte hain."],
     "responses_en": ["Data Science is the field of extracting insights from data using statistics and programming.", "In Data Science, we analyze large datasets to find patterns."]},

    {"category": "tech", "patterns": ["what is neural network"],
     "responses_ur": ["Neural Network, insani dimagh se inspired ek computing system hai jo AI mein use hota hai.", "Neural Networks layers of nodes hotay hain jo data process karte hain."],
     "responses_en": ["A Neural Network is a computing system inspired by the human brain, used in AI.", "Neural Networks are layers of nodes that process data."]},

    {"category": "tech", "patterns": ["what is open source"],
     "responses_ur": ["Open Source software wo hota hai jiska code publicly available hota hai modify karne ke liye.", "Open source projects mein koi bhi contribute kar sakta hai."],
     "responses_en": ["Open Source software has publicly available code that anyone can modify.", "Anyone can contribute to open source projects."]},

    {"category": "tech", "patterns": ["what is git"],
     "responses_ur": ["Git ek version control system hai jo code changes track karta hai.", "Git developers ko collaborate karne aur code history manage karne mein madad karta hai."],
     "responses_en": ["Git is a version control system that tracks code changes.", "Git helps developers collaborate and manage code history."]},

    {"category": "tech", "patterns": ["what is web scraping"],
     "responses_ur": ["Web Scraping websites se data automatically extract karne ka process hai.", "Web scraping mein hum HTML se useful information nikaltay hain, jaise BeautifulSoup se."],
     "responses_en": ["Web Scraping is the process of automatically extracting data from websites.", "Web scraping pulls useful information from HTML, like with BeautifulSoup."]},

    {"category": "tech", "patterns": ["what is beautifulsoup"],
     "responses_ur": ["BeautifulSoup ek Python library hai jo HTML/XML parsing ke liye use hoti hai.", "BeautifulSoup web scraping mein data extract karne ke liye popular hai."],
     "responses_en": ["BeautifulSoup is a Python library used for parsing HTML/XML.", "BeautifulSoup is popular for extracting data in web scraping."]},

    {"category": "tech", "patterns": ["what is tkinter"],
     "responses_ur": ["Tkinter, Python ki built-in library hai GUI applications banane ke liye.", "Tkinter se hum desktop apps ke liye windows aur buttons bana saktay hain."],
     "responses_en": ["Tkinter is Python's built-in library for building GUI applications.", "Tkinter lets us build windows and buttons for desktop apps."]},

    # CATEGORY 9: MOTIVATIONAL / ADVICE (20 entries)
    {"category": "motivation", "patterns": ["motivate me", "mujhe motivate karo"],
     "responses_ur": ["Aap jo bhi kar rahe hain, wo bohot acha hai — bas consistency rakhein!", "Har chota kadam aapko manzil ke qareeb le jata hai, himmat na harein!"],
     "responses_en": ["Whatever you're doing, you're doing great — just stay consistent!", "Every small step brings you closer to your goal, don't give up!"]},

    {"category": "motivation", "patterns": ["give me advice", "koi advice do"],
     "responses_ur": ["Roz thora thora seekhein, consistency hi success ki chabi hai.", "Apne kaam par focus rakhein, natije khud aayenge."],
     "responses_en": ["Learn a little every day, consistency is the key to success.", "Stay focused on your work, results will follow."]},

    {"category": "motivation", "patterns": ["i want to give up", "hosla haar raha hoon"],
     "responses_ur": ["Ruko mat! Jo mushkil waqt hai wo guzar jayega.", "Har successful insan ne mushkil waqt dekha hai, aap bhi kar loge!"],
     "responses_en": ["Don't stop! This hard time will pass.", "Every successful person has faced tough times, you'll make it too!"]},

    {"category": "motivation", "patterns": ["i failed", "main fail ho gaya"],
     "responses_ur": ["Failure sirf ek lesson hai, ye success ka rasta hai.", "Har fail hona ek naya seekhne ka moka hai, himmat rakhein!"],
     "responses_en": ["Failure is just a lesson, it's part of the path to success.", "Every failure is a chance to learn something new, stay strong!"]},

    {"category": "motivation", "patterns": ["i cant do this", "mujh se nahi hoga"],
     "responses_ur": ["Aap kar saktay hain! Bas ek kadam aage badhein.", "Believe in yourself, aap capable hain!"],
     "responses_en": ["You can do this! Just take one step forward.", "Believe in yourself, you're capable!"]},

    {"category": "motivation", "patterns": ["how to stay focused", "focus kaise rakhein"],
     "responses_ur": ["Chotay goals set karein aur ek waqt mein ek kaam par focus karein.", "Distractions door rakhein aur apna schedule follow karein."],
     "responses_en": ["Set small goals and focus on one task at a time.", "Keep distractions away and follow your schedule."]},

    {"category": "motivation", "patterns": ["success tips", "kamyabi ke tips"],
     "responses_ur": ["Consistency, hard work, aur patience — yehi success ka formula hai.", "Roz thora improve karein, kamyabi khud chal kar aayegi."],
     "responses_en": ["Consistency, hard work, and patience — that's the formula for success.", "Improve a little every day, success will follow."]},

    {"category": "motivation", "patterns": ["i am stuck", "main atak gaya hoon"],
     "responses_ur": ["Break lein, phir naye zaviye se dekhein masla.", "Kisi se help lein, atakna normal hai, ruk mat jayen."],
     "responses_en": ["Take a break, then look at the problem from a new angle.", "Ask someone for help, getting stuck is normal, don't stop."]},

    {"category": "motivation", "patterns": ["quote of the day", "aaj ka quote"],
     "responses_ur": ["Success is not final, failure is not fatal: it is the courage to continue that counts.", "Believe you can and you're halfway there."],
     "responses_en": ["Success is not final, failure is not fatal: it is the courage to continue that counts.", "Believe you can and you're halfway there."]},

    {"category": "motivation", "patterns": ["inspire me", "mujhe inspire karo"],
     "responses_ur": ["Aap khud ek inspiration hain jo naye skills seekh rahe hain!", "Har din ek nayi shuruaat hai, aage badhte rahein!"],
     "responses_en": ["You're already an inspiration for learning new skills!", "Every day is a fresh start, keep moving forward!"]},

    {"category": "motivation", "patterns": ["how to be productive", "productive kaise banein"],
     "responses_ur": ["To-do list banayein aur priorities set karein.", "Distractions kam karein aur ek waqt mein ek task par focus karein."],
     "responses_en": ["Make a to-do list and set priorities.", "Reduce distractions and focus on one task at a time."]},

    {"category": "motivation", "patterns": ["how to learn faster", "jaldi seekhne ka tareeka"],
     "responses_ur": ["Practice roz karein aur real projects par kaam karein.", "Concepts ko implement kar ke seekhna sabse acha tareeka hai."],
     "responses_en": ["Practice daily and work on real projects.", "The best way to learn is by implementing concepts hands-on."]},

    {"category": "motivation", "patterns": ["im feeling lazy", "sustee ho rahi hai"],
     "responses_ur": ["Chota sa kaam start karein, momentum khud ban jayega.", "5 minute ka rule try karein — sirf 5 minute kaam karein, phir dekhein!"],
     "responses_en": ["Start with a small task, momentum will build.", "Try the 5-minute rule — just work for 5 minutes, then see!"]},

    {"category": "motivation", "patterns": ["exam stress", "exam ka stress"],
     "responses_ur": ["Thora thora roz parhein, last minute cramming se bachein.", "Deep breaths lein aur apni preparation par bharosa rakhein."],
     "responses_en": ["Study a little every day, avoid last-minute cramming.", "Take deep breaths and trust your preparation."]},

    {"category": "motivation", "patterns": ["how to build confidence", "confidence kaise banayein"],
     "responses_ur": ["Chotay achievements celebrate karein aur khud par yaqeen rakhein.", "Practice se confidence khud ba khud aata hai."],
     "responses_en": ["Celebrate small achievements and believe in yourself.", "Confidence naturally builds with practice."]},

    {"category": "motivation", "patterns": ["never give up"],
     "responses_ur": ["Bilkul sahi! Consistency hi kamyabi ki chabi hai.", "Himmat na harein, manzil qareeb hai!"],
     "responses_en": ["Exactly right! Consistency is the key to success.", "Don't lose hope, the goal is near!"]},

    {"category": "motivation", "patterns": ["how to manage time", "time kaise manage karein"],
     "responses_ur": ["Priorities set karein aur schedule banayein.", "Important kaam pehle karein, phir baaki cheezein."],
     "responses_en": ["Set priorities and make a schedule.", "Do the important tasks first, then everything else."]},

    {"category": "motivation", "patterns": ["im procrastinating", "kaam taal raha hoon"],
     "responses_ur": ["Chota sa step lein abhi, procrastination khatam ho jayegi.", "Ek timer laga kar 10 minute ke liye kaam shuru karein."],
     "responses_en": ["Take a small step right now, procrastination will fade.", "Set a timer and work for just 10 minutes to start."]},

    {"category": "motivation", "patterns": ["life advice", "zindagi ki advice"],
     "responses_ur": ["Apne aap par invest karein, seekhna kabhi na chorein.", "Patience rakhein, achi cheezein waqt lagti hain."],
     "responses_en": ["Invest in yourself, never stop learning.", "Be patient, good things take time."]},

    {"category": "motivation", "patterns": ["how to overcome fear", "dar kaise dur karein"],
     "responses_ur": ["Chotay chotay steps lein, dar khud kam ho jayega.", "Jis cheez se dar lagta hai usay bar bar karein, dar khatam ho jayega."],
     "responses_en": ["Take small steps, fear will naturally reduce.", "Face what scares you repeatedly, the fear will fade."]},

    # CATEGORY 10: HELP & BOT CAPABILITIES (21 entries)
    {"category": "help", "patterns": ["help", "madad karo"],
     "responses_ur": ["Zaroor! Bataiye kya madad chahiye.", "Main yahan hoon aapki madad ke liye, bataiye kya chahiye."],
     "responses_en": ["Sure! Tell me what you need help with.", "I'm here to help, just tell me what you need."]},

    {"category": "help", "patterns": ["what can i ask you", "kya pooch sakta hoon"],
     "responses_ur": ["Aap mujh se general sawal, jokes, motivation, ya kuch bhi pooch saktay hain! Agar mujhe pata na hua to main Wikipedia se dhoondh kar bataunga.", "Kuch bhi pooch sakte hain, agar mujhe pata na hua to main search kar ke bataunga!"],
     "responses_en": ["You can ask me general questions, jokes, motivation, or anything! If I don't know, I'll look it up on Wikipedia.", "Ask me anything, if I don't know I'll search and tell you!"]},

    {"category": "help", "patterns": ["how do you work", "aap kaise kaam karte hain"],
     "responses_ur": ["Main pehle apne fixed responses check karta hoon, agar match na ho to Wikipedia se info la kar deta hoon.", "Main keywords match karta hoon aapke sawal mein, phir relevant jawab deta hoon."],
     "responses_en": ["I first check my fixed responses, and if there's no match I fetch info from Wikipedia.", "I match keywords in your question, then give a relevant response."]},

    {"category": "help", "patterns": ["can you search the internet", "kya aap internet search kar saktay hain"],
     "responses_ur": ["Ji haan! Agar mujhe pehle se jawab nahi pata, to main Wikipedia se search kar leta hoon.", "Bilkul, unknown queries ke liye main Wikipedia scrape karta hoon."],
     "responses_en": ["Yes! If I don't already know the answer, I search Wikipedia.", "Absolutely, I scrape Wikipedia for unknown queries."]},

    {"category": "help", "patterns": ["i need assistance", "mujhe madad chahiye"],
     "responses_ur": ["Bataiye kis cheez mein madad chahiye.", "Main yahan hoon, bataiye kya problem hai."],
     "responses_en": ["Tell me what you need help with.", "I'm here, tell me the problem."]},

    {"category": "help", "patterns": ["can you help me with homework", "homework mein madad karo"],
     "responses_ur": ["Main koshish kar sakta hoon! Bataiye kis subject ka homework hai.", "Zaroor, bataiye kya sawal hai."],
     "responses_en": ["I can try! Tell me which subject the homework is for.", "Sure, tell me the question."]},

    {"category": "help", "patterns": ["what topics can you discuss"],
     "responses_ur": ["Main general knowledge, tech, motivation, jokes, aur bohot kuch discuss kar sakta hoon!", "Kuch bhi topic ho, main try karunga help karne ki."],
     "responses_en": ["I can discuss general knowledge, tech, motivation, jokes, and much more!", "Whatever the topic, I'll try to help."]},

    {"category": "help", "patterns": ["how to use you", "aap ko kaise use karein"],
     "responses_ur": ["Bas apna sawal type karein aur enter dabayen!", "Simple hai, message likhein aur send karein."],
     "responses_en": ["Just type your question and hit enter!", "Simple, write a message and hit send."]},

    {"category": "help", "patterns": ["can you answer everything", "kya aap har sawal ka jawab de saktay hain"],
     "responses_ur": ["Main koshish karta hoon, aur agar na pata ho to Wikipedia se dhoondh leta hoon!", "Har sawal ka jawab nahi, lekin bohot se sawalon mein madad kar sakta hoon."],
     "responses_en": ["I try my best, and if I don't know I search Wikipedia!", "Not every question, but I can help with a lot of them."]},

    {"category": "help", "patterns": ["im stuck", "atak gaya hoon"],
     "responses_ur": ["Bataiye kahan atak gaye hain, main madad karta hoon.", "Koi baat nahi, step by step batayen kya masla hai."],
     "responses_en": ["Tell me where you're stuck, I'll help.", "No worries, tell me the issue step by step."]},

    {"category": "help", "patterns": ["how accurate are you", "kitne accurate hain aap"],
     "responses_ur": ["Main apni best koshish karta hoon, lekin important cheezon ke liye verify zaroor karein.", "Accuracy achi hai, lekin critical decisions ke liye reliable source check karein."],
     "responses_en": ["I do my best, but always verify important information.", "My accuracy is decent, but check a reliable source for critical decisions."]},

    {"category": "help", "patterns": ["can you give examples", "examples de saktay hain"],
     "responses_ur": ["Zaroor, bataiye kis cheez ka example chahiye.", "Bilkul, thora specify karein topic."],
     "responses_en": ["Sure, tell me what you need an example of.", "Absolutely, just specify the topic."]},

    {"category": "help", "patterns": ["explain this to me"],
     "responses_ur": ["Zaroor, bataiye kya explain karna hai.", "Bataiye kis cheez ke baare mein samjhna hai."],
     "responses_en": ["Sure, tell me what to explain.", "Tell me what you'd like to understand."]},

    {"category": "help", "patterns": ["can you teach me", "sikha saktay hain"],
     "responses_ur": ["Koshish kar sakta hoon! Bataiye kya seekhna chahte hain.", "Zaroor, topic bataiye."],
     "responses_en": ["I can try! Tell me what you'd like to learn.", "Sure, just tell me the topic."]},

    {"category": "help", "patterns": ["im lost", "kho gaya hoon"],
     "responses_ur": ["Koi baat nahi, bataiye kya cheez samajh nahi aa rahi.", "Step by step batayen, main madad karta hoon."],
     "responses_en": ["No worries, tell me what's confusing you.", "Walk me through it step by step, I'll help."]},

    {"category": "help", "patterns": ["what should i ask"],
     "responses_ur": ["Kuch bhi pooch sakte hain - general knowledge, tech, ya casual baatein!", "Jo bhi mann mein aaye, pooch lein!"],
     "responses_en": ["Ask anything — general knowledge, tech, or just casual chat!", "Ask whatever's on your mind!"]},

    {"category": "help", "patterns": ["are you reliable", "kya aap reliable hain"],
     "responses_ur": ["Main apni best koshish karta hoon, lekin hamesha double-check karna acha practice hai.", "Reliable hoon apni jagah, but verify important info kahin aur bhi."],
     "responses_en": ["I do my best, but double-checking is always good practice.", "I'm reliable in my own way, but verify important info elsewhere too."]},

    {"category": "help", "patterns": ["can you solve problems", "masail hal kar saktay hain"],
     "responses_ur": ["Koshish kar sakta hoon, bataiye kya masla hai.", "Zaroor, bataiye kya problem hai."],
     "responses_en": ["I can try, tell me the issue.", "Sure, tell me the problem."]},

    {"category": "help", "patterns": ["do you understand urdu", "urdu samajhtay hain"],
     "responses_ur": ["Ji haan, main Roman Urdu samajh sakta hoon!", "Bilkul, Urdu aur English dono samajh leta hoon."],
     "responses_en": ["Yes, I understand Roman Urdu!", "Absolutely, I understand both Urdu and English."]},

    {"category": "help", "patterns": ["can i talk in urdu", "urdu mein baat kar sakta hoon"],
     "responses_ur": ["Bilkul, Roman Urdu mein baat karein, koi masla nahi!", "Ji haan, freely Urdu mein baat karein."],
     "responses_en": ["Sure, feel free to talk in Roman Urdu, no problem!", "Yes, feel free to speak in Urdu."]},

    {"category": "help", "patterns": ["restart", "phir se shuru karo"],
     "responses_ur": ["Theek hai, chaliye phir se shuru karte hain!", "Restart ho gaya, bataiye kya poochna hai."],
     "responses_en": ["Okay, let's start over!", "Restarted, tell me what you'd like to ask."]},

    # CATEGORY 11: RANDOM KNOWLEDGE / FUN FACTS (20 entries)
    {"category": "facts", "patterns": ["tell me a fact", "koi fact batao"],
     "responses_ur": ["Honey kabhi kharab nahi hota, hazaron saal purani honey bhi khane laiq hoti hai!", "Octopus ke teen dil hotay hain!"],
     "responses_en": ["Honey never spoils — even honey thousands of years old is still edible!", "Octopuses have three hearts!"]},

    {"category": "facts", "patterns": ["fun fact", "mazedar fact"],
     "responses_ur": ["Bananas berries hain lekin strawberries nahi!", "Ek din mein insaan ka dimagh 50,000 se zyada thoughts generate karta hai!"],
     "responses_en": ["Bananas are berries, but strawberries aren't!", "The human brain generates over 50,000 thoughts a day!"]},

    {"category": "facts", "patterns": ["do you know any facts"],
     "responses_ur": ["Haan, kaafi facts pata hain, sunayen?", "Zaroor, thora bataiye konsi field ka fact chahiye - space, animals, ya history?"],
     "responses_en": ["Yes, I know quite a few, want to hear one?", "Sure, tell me which topic — space, animals, or history?"]},

    {"category": "facts", "patterns": ["space fact", "space ka fact batao"],
     "responses_ur": ["Space mein awaz nahi hoti kyunki wahan air nahi hai!", "Ek din Venus par Earth ke ek saal se zyada lamba hota hai!"],
     "responses_en": ["Sound doesn't travel in space because there's no air!", "A day on Venus is longer than a year on Earth!"]},

    {"category": "facts", "patterns": ["animal fact", "janwar ka fact"],
     "responses_ur": ["Cheetahs sirf 3 seconds mein 0 se 60 mph ki speed pakar saktay hain!", "Elephants akela jaanwar hai jo koodh nahi sakta!"],
     "responses_en": ["Cheetahs can go from 0 to 60 mph in just 3 seconds!", "Elephants are the only animal that can't jump!"]},

    {"category": "facts", "patterns": ["history fact", "tareekh ka fact"],
     "responses_ur": ["Great Wall of China itni lambi hai ke space se bhi dikhne ka myth famous hai (haqeeqat mein ye myth hai)!", "Pyramids of Egypt, mammoths ke extinct hone se bhi pehle bane thay!"],
     "responses_en": ["There's a famous myth that the Great Wall of China is visible from space (it's actually just a myth)!", "The Egyptian pyramids were built before mammoths went extinct!"]},

    {"category": "facts", "patterns": ["science fact", "science ka fact"],
     "responses_ur": ["Insani jism mein itni carbon hai jo 900 pencils bana sakti hai!", "Lightning, sun ki surface se 5 guna zyada garam hoti hai!"],
     "responses_en": ["The human body contains enough carbon to make 900 pencils!", "Lightning is 5 times hotter than the surface of the sun!"]},

    {"category": "facts", "patterns": ["math fact", "math ka fact"],
     "responses_ur": ["Zero ek number hai jo kisi bhi qadeem tehzeeb mein directly invent nahi hua tha, iski history interesting hai!", "Pi (\u03c0) ek infinite, non-repeating number hai!"],
     "responses_en": ["Zero has a fascinating history — it wasn't invented right away by ancient civilizations!", "Pi (\u03c0) is an infinite, non-repeating number!"]},

    {"category": "facts", "patterns": ["computer fact", "computer ka fact"],
     "responses_ur": ["Pehla computer bug ek asli keera (insect) tha jo machine mein phans gaya tha!", "The first computer programmer thi ek khatoon, Ada Lovelace!"],
     "responses_en": ["The first computer 'bug' was an actual insect stuck in a machine!", "The first computer programmer was a woman, Ada Lovelace!"]},

    {"category": "facts", "patterns": ["pakistan fact", "pakistan ka fact"],
     "responses_ur": ["Pakistan mein duniya ki dusri sab se buland chotti K2 hai!", "Pakistan ka national game hockey hai!"],
     "responses_en": ["Pakistan is home to K2, the world's second-highest peak!", "Pakistan's national sport is hockey!"]},

    {"category": "facts", "patterns": ["food fact", "khanay ka fact"],
     "responses_ur": ["Apples paani mein doob nahi saktay kyunki unmein 25% air hoti hai!", "Chocolate kabhi kabhi kutton ke liye zeher ban sakti hai!"],
     "responses_en": ["Apples float in water because they're 25% air!", "Chocolate can be toxic to dogs!"]},

    {"category": "facts", "patterns": ["ocean fact", "samandar ka fact"],
     "responses_ur": ["Humne moon ki surface se zyada samandar ki tehh explore nahi ki!", "Blue whale duniya ka sab se bara jaanwar hai!"],
     "responses_en": ["We've explored more of the moon's surface than the ocean floor!", "The blue whale is the largest animal on Earth!"]},

    {"category": "facts", "patterns": ["human body fact", "jism ka fact"],
     "responses_ur": ["Insani dil roz taqreeban 100,000 dafa dharakta hai!", "Aapki skin har 27 din mein khud ko replace karti hai!"],
     "responses_en": ["The human heart beats about 100,000 times a day!", "Your skin replaces itself every 27 days!"]},

    {"category": "facts", "patterns": ["language fact", "zaban ka fact"],
     "responses_ur": ["Duniya mein taqreeban 7000 languages boli jati hain!", "Mandarin Chinese duniya ki sab se zyada boli jane wali language hai."],
     "responses_en": ["There are around 7,000 languages spoken in the world!", "Mandarin Chinese is the most spoken language in the world."]},

    {"category": "facts", "patterns": ["technology fact", "technology ka fact"],
     "responses_ur": ["Pehla mobile phone ka wazan 1 kg se zyada tha!", "Internet ki speed hamesha barh rahi hai, 5G ab common ho raha hai."],
     "responses_en": ["The first mobile phone weighed over 1 kg!", "Internet speeds keep growing, 5G is now common."]},

    {"category": "facts", "patterns": ["random fact"],
     "responses_ur": ["Sharks dinosaurs se bhi purane hain!", "Ek group of flamingos ko 'flamboyance' kaha jata hai!"],
     "responses_en": ["Sharks are older than dinosaurs!", "A group of flamingos is called a 'flamboyance'!"]},

    {"category": "facts", "patterns": ["cool fact"],
     "responses_ur": ["Aapke naakhun aapki ungliyon se tezi se barhtay hain!", "Ek group of crows ko 'murder' kaha jata hai!"],
     "responses_en": ["Your fingernails grow faster than your toenails!", "A group of crows is called a 'murder'!"]},

    {"category": "facts", "patterns": ["weird fact"],
     "responses_ur": ["Bananas radioactive hoti hain, magar bohot kam matra mein!", "Insan aur giraffe ki gardan mein bones ki tadad barabar hoti hai - 7!"],
     "responses_en": ["Bananas are slightly radioactive, but only in tiny amounts!", "Humans and giraffes have the same number of neck bones — 7!"]},

    {"category": "facts", "patterns": ["interesting fact"],
     "responses_ur": ["Eiffel Tower garmi mein thora bara ho jata hai metal ke expansion ki wajah se!", "Duniya ka sab se pehla email 1971 mein bheja gaya tha!"],
     "responses_en": ["The Eiffel Tower grows slightly taller in summer due to metal expansion!", "The world's first email was sent in 1971!"]},

    {"category": "facts", "patterns": ["do you know trivia", "trivia pata hai"],
     "responses_ur": ["Haan, kaafi trivia pata hai, konsa topic chahiye?", "Zaroor! Konsi category mein trivia chahiye?"],
     "responses_en": ["Yes, I know quite a bit of trivia, which topic?", "Sure! Which category would you like trivia on?"]},

    # CATEGORY 12: EMOTIONAL SUPPORT (15 entries)
    {"category": "emotional", "patterns": ["im depressed", "dil udaas hai"],
     "responses_ur": ["Aap akele nahi hain, kisi apne se baat zaroor karein, ye help karta hai.", "Ye feelings temporary hain, kisi trusted insaan se baat karein ya professional se madad lein."],
     "responses_en": ["You're not alone, please talk to someone close to you, it helps.", "These feelings are temporary, talk to someone you trust or seek professional help."]},

    {"category": "emotional", "patterns": ["i feel like giving up", "haar mann rahi hai"],
     "responses_ur": ["Please himmat na harein, mushkil waqt guzar jata hai. Kisi se baat karna acha rahega.", "Aap important hain, kisi qareebi se baat zaroor karein."],
     "responses_en": ["Please don't give up, hard times pass. It would help to talk to someone.", "You matter, please talk to someone close to you."]},

    {"category": "emotional", "patterns": ["nobody understands me", "koi mujhe samajhta nahi"],
     "responses_ur": ["Aisa mehsoos hona mushkil hota hai, koi trusted dost ya family member se baat karein.", "Aapki feelings valid hain, kisi se share karna madadgar ho sakta hai."],
     "responses_en": ["That's a hard feeling to sit with, talk to a trusted friend or family member.", "Your feelings are valid, sharing them can really help."]},

    {"category": "emotional", "patterns": ["im overwhelmed", "sab kuch bohot zyada lag raha hai"],
     "responses_ur": ["Ek waqt mein ek kaam par focus karein, sab manageable ho jayega.", "Break lein, deep breath lein, sab theek ho jayega."],
     "responses_en": ["Focus on one thing at a time, it'll become manageable.", "Take a break, breathe deeply, it'll be okay."]},

    {"category": "emotional", "patterns": ["i feel hopeless", "koi umeed nahi"],
     "responses_ur": ["Aapki feelings important hain, please kisi trusted insaan ya professional se baat karein.", "Ye mushkil waqt hai, lekin akele iska samna na karein, madad lein."],
     "responses_en": ["Your feelings matter, please talk to someone you trust or a professional.", "This is a hard time, but don't face it alone, please seek help."]},

    {"category": "emotional", "patterns": ["i need someone to talk to", "kisi se baat karni hai"],
     "responses_ur": ["Main yahan hoon sunne ke liye, lekin kisi qareebi insaan se bhi zaroor baat karein.", "Bataiye kya chal raha hai, main sun raha hoon."],
     "responses_en": ["I'm here to listen, but please also talk to someone close to you.", "Tell me what's going on, I'm listening."]},

    {"category": "emotional", "patterns": ["im not okay", "main theek nahi hoon"],
     "responses_ur": ["Sorry sun kar, kya hua? Kisi se baat karna madadgar ho sakta hai.", "Aap akele nahi hain, please kisi trusted insaan se baat karein."],
     "responses_en": ["I'm sorry to hear that, what happened? Talking to someone might help.", "You're not alone, please talk to someone you trust."]},

    {"category": "emotional", "patterns": ["i cant cope", "sambhal nahi pa raha"],
     "responses_ur": ["Ye bohot mushkil lag sakta hai, please kisi professional ya qareebi se madad lein.", "Aap akele nahi hain is mein, baat karna zaroori hai kisi se."],
     "responses_en": ["This can feel very hard, please seek help from a professional or someone close.", "You're not alone in this, it's important to talk to someone."]},

    {"category": "emotional", "patterns": ["i feel empty", "khaali khaali mehsoos hota hai"],
     "responses_ur": ["Ye feelings mushkil hoti hain, kisi se baat karna madadgar ho sakta hai.", "Please apne feelings kisi trusted insaan se share karein."],
     "responses_en": ["These feelings are tough, talking to someone might help.", "Please share what you're feeling with someone you trust."]},

    {"category": "emotional", "patterns": ["everything is wrong", "sab kuch ghalat ja raha hai"],
     "responses_ur": ["Mushkil waqt hai, lekin ye guzar jayega. Kisi se baat karein.", "Ek ek kaam par focus karein, sab theek ho jayega dheere dheere."],
     "responses_en": ["This is a hard time, but it will pass. Talk to someone.", "Focus on one thing at a time, it'll get better gradually."]},

    {"category": "emotional", "patterns": ["i miss someone", "kisi ki yaad aa rahi hai"],
     "responses_ur": ["Kisi ki yaad aana normal hai, unse contact karne ki koshish karein agar mumkin ho.", "Ye feelings normal hain, apna khayal rakhein."],
     "responses_en": ["Missing someone is normal, try reaching out to them if possible.", "These feelings are normal, take care of yourself."]},

    {"category": "emotional", "patterns": ["im scared", "dar lag raha hai"],
     "responses_ur": ["Dar lagna normal hai, deep breaths lein aur kisi se apni feelings share karein.", "Aap akele nahi hain, baat karein kisi trusted insaan se."],
     "responses_en": ["Feeling scared is normal, take deep breaths and share your feelings with someone.", "You're not alone, talk to someone you trust."]},

    {"category": "emotional", "patterns": ["i feel anxious", "anxiety ho rahi hai"],
     "responses_ur": ["Deep breaths lein, ye feeling guzar jayegi. Zaroorat ho to professional se madad lein.", "Anxiety mushkil hoti hai, please apna khayal rakhein aur kisi se baat karein."],
     "responses_en": ["Take deep breaths, this feeling will pass. Seek professional help if needed.", "Anxiety is hard, please take care of yourself and talk to someone."]},

    {"category": "emotional", "patterns": ["thank you for listening", "sunne ka shukriya"],
     "responses_ur": ["Hamesha yahan hoon sunne ke liye.", "Koi baat nahi, apna khayal rakhein."],
     "responses_en": ["I'm always here to listen.", "No problem, take care of yourself."]},

    {"category": "emotional", "patterns": ["i feel better now", "ab acha mehsoos ho raha hai"],
     "responses_ur": ["Ye sun kar bohot khushi hui!", "Great! Apna khayal rakhna hamesha."],
     "responses_en": ["That makes me really happy to hear!", "Great! Always take care of yourself."]},
]

# Total entries count (for verification)
TOTAL_ENTRIES = len(QA_DATABASE)

if __name__ == "__main__":
    print(f"Total Q&A entries: {TOTAL_ENTRIES}")
    categories = set(entry["category"] for entry in QA_DATABASE)
    print(f"Total categories: {len(categories)}")
    for cat in categories:
        count = sum(1 for entry in QA_DATABASE if entry["category"] == cat)
        print(f"  - {cat}: {count} entries")
