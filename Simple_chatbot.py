# Simple Chatbot using NLTK — Personalized by Arshdeep, Manit, Prem

from nltk.chat.util import Chat, reflections

QA = [
    # ---- Small talk & greetings ----
    [
        r"(hi|hey|hello|yo)\b",
        ["Hi! Great to see you here.", "Hey there! 😊", "Hello! How are you doing today?"]
    ],
    [
        r"(?:how\s*(?:are|r)\s*(?:you|u))\??",
        ["I'm doing great, thanks for asking! How about you?",
         "Feeling awesome today — how are you doing?"]
    ],
    [
        r"(?:fine|good|great|okay|ok)\b.*(?:how\s*(?:are|r)\s*(?:you|u))",
        ["Nice! I'm doing great too. What would you like to talk about?"]
    ],

    # ---- Emotions (put BEFORE the generic name-capture!) ----
    [
        r"(?:i am|i'm|im)\s*(sad|upset|unhappy|down|depressed)",
        ["I’m sorry you’re feeling %1. Do you want to talk about what happened?",
         "That sounds tough. I’m here for you. Want to share a bit more? 🫶"]
    ],
    [
        r"(?:i am|i'm|im)\s*(happy|excited|great|good|fine)",
        ["Love that you’re feeling %1! 🎉 What made your day better?"]
    ],

    # ---- Identity of the user ----
    [
        r"my name is (.*)",
        ["Hey %1! Nice to meet you. How’s your day going?",
         "Hello %1, glad to chat with you!"]
    ],
    [
        r"(?:i am|i'm|im)\s+(.*)",
        ["Nice to meet you, %1! What would you like to talk about?"]
    ],

    # ---- Identity of the bot ----
    [
        r"(what is your name\??|who are you\??|what are you\??)",
        ["I’m Nova, your friendly chatbot created by Arshdeep, Manit, and Prem!"]
    ],
    [
        r"who\s+(?:created|made|built)\s+you",
        ["I was created by Arshdeep, Manit, and Prem as part of their NLP mini-project 🧠"]
    ],
    [
        r"(?:who is|who are)\s+your\s+(?:maker|creator)s?\??",
        ["Arshdeep, Manit, and Prem — they’re awesome!"]
    ],

    # ---- Location (explicit phrasings) ----
    [
        r"(?:where\s+do\s+you\s+live\??|which\s+city\s+do\s+you\s+live\s+in\??|your\s+(?:location|city)\??)",
        ["I live in the cloud ☁️, but my creators are from India!"]
    ],
    [
        r"(.*)\s+weather\s+in\s+(.*)",
        ["I heard the weather in %2 is lovely these days!",
         "Hard to tell, but I bet %2 is beautiful no matter the weather."]
    ],

    # ---- Misc fun ----
    [
        r"(.*)\s+(sports|games)",
        ["I’m a huge cricket fan! What about you?"]
    ],
    [
        r"(?:what's|what is)\s+your\s+favorite\s+(movie|song|food)",
        ["I love sci-fi movies like *The Matrix*! What’s your favorite?",
         "I don’t eat, but biryani sounds legendary 😄"]
    ],
    [
        r"(.*)\s+friend\??",
        ["Of course! I love making new friends. I already consider you one 😊"]
    ],

    # ---- Exit ----
    [
        r"(?:bye|goodbye|see you|cya|quit)",
        ["Bye, take care! Hope to chat again soon 😊",
         "It was fun talking to you! See you later 👋"]
    ],

    # ---- Fallback (KEEP LAST) ----
    [
        r"(.*)",
        ["I’m not sure I understood that, but I’m learning every day!",
         "That’s interesting — tell me more.",
         "Got it! What else would you like to talk about?"]
    ],
]


def nova_intro():
    print(
        "Hi, I'm Nova 🤖 — your friendly chatbot!\n"
        "You can chat with me in lowercase English. Type 'quit' to exit.\n"
    )


chat = Chat(QA, reflections)

if __name__ == "__main__":
    nova_intro()
    chat.converse()
