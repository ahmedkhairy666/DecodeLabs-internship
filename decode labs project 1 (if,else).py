print("AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("AI Chatbot: Hello! How can I help you?")
    
    elif user in ["how are you", "how are you doing"]:
        print("AI Chatbot: I'm doing great!")
    
    elif user in ["what is your name", "who are you"]:
        print("AI Chatbot: I am a rule-based AI chatbot.")
    
    elif user in ["who created you"]:
        print("Eng.Ahmed Khairy.")
    
    
    elif user in ["bye", "exit", "quit"]:
        print("AI Chatbot: Goodbye!")
        break
    
    else:
        print("AI Chatbot: Sorry, I don't understand that.")