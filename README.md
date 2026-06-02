# DecodeLabs_tasks

RESPONSES = {
    "hello":        "Hey there! 👋 I'm DecoBot. How can I help you today?",
    "hi":           "Hi! Great to meet you. What's on your mind?",
    "hey":          "Hey! What can I do for you?",
    "bye":          "Goodbye! Keep building great things. 🚀",
    "goodbye":      "See you later! Don't forget to push your code. 😄",
    "who are you":  "I'm DecoBot — a rule-based AI chatbot built at DecodeLabs!",
    "what are you": "I'm a deterministic chatbot. Pure logic, zero hallucinations. 🤖",
    "who created you": "Eng.Ahmed Khairy",
    "what is decodelabs": "DecodeLabs is an AI training platform that teaches real-world engineering skills through hands-on projects.",
    "tell me about decodelabs": "DecodeLabs, based in Greater Lucknow, India, runs industrial AI training programs. You're in Batch 2026!",
    "what is this project":  "This is Project 1: The Rule-Based AI Chatbot. It teaches control flow, decision-making logic, and basic AI concepts.",
    "what is project 1":     "Project 1 is your foundation phase — mastering if-else logic and dictionary lookups before diving into deep learning.",
    "what is ai":            "AI stands for Artificial Intelligence — systems that simulate human-like decision making. You're building one right now!",
    "what is a chatbot":     "A chatbot is a program that simulates conversation. Rule-based bots like me use exact logic; LLMs use probability.",
    "what is an llm":        "An LLM (Large Language Model) is a probabilistic AI — it predicts the most likely next word. Unlike me, it can hallucinate!",
    "difference between rule based and llm": "Rule-based = deterministic (always same output). LLM = probabilistic (output can vary). Both have their place in modern AI systems!",
    "help":   "You can ask me: 'who are you', 'what is AI', 'what is this project', 'tell me about DecodeLabs', and more. Type 'quit' to exit.",
    "menu":   "Topics I know: greetings, farewells, AI concepts, DecodeLabs info, project info. Try any of them!",
    "how are you":  "I'm running at O(1) speed and feeling great! Thanks for asking. ⚡",
    "are you human":"Nope! I'm 100% hard-coded logic — no neurons, just Python dictionaries. 😎",
    "tell me a joke":"Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
}

FAREWELL_TRIGGERS = {"quit", "exit", "bye", "goodbye"}
FAREWELL_MESSAGE  = "👋 Shutting down DecoBot. See you next session!"
FALLBACK = "🤔 I don't understand that yet. Try 'help' to see what I know."

BANNER = """
╔══════════════════════════════════════════════════════╗
║        DecodeLabs — Project 1: DecodeBot 🤖          ║   
║        Rule-Based AI Chatbot  |  Batch 2026          ║
║  Type 'help' for topics  |  Type 'quit' to exit      ║
╚══════════════════════════════════════════════════════╝
"""

def sanitize(raw):
    return raw.lower().strip()

def get_response(clean_input):
    return RESPONSES.get(clean_input, FALLBACK)

def run_chatbot():
    print(BANNER)
    while True:
        raw_input = input("You: ")
        clean_input = sanitize(raw_input)
        if clean_input in FAREWELL_TRIGGERS:
            print(f"DecoBot: {FAREWELL_MESSAGE}")
            break
        reply = get_response(clean_input)
        print(f"DecoBot: {reply}\n")

if __name__ == "__main__":
    run_chatbot()
