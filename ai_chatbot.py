def chatbot():
    print("Chatbot: Hey! I'm your chatbot.")

    name = input("Chatbot: What's your name? ")
    print(f"Chatbot: Nice to meet you, {name}!")

    print("Chatbot: Type 'bye', 'exit', or 'quit' to exit.")

    while True:
        message = input("You: ").strip().lower()

        # Updated exit conditions
        if message in ("bye", "exit", "quit"):
            print(f"Chatbot: Goodbye, {name}!")
            break

        # Expanded greetings using a tuple
        elif message in ("hello", "hi", "hey", "greetings", "sup", "what's up"):
            print(f"Chatbot: Hey {name}! How are you doing today?")

        elif message in ("how are you", "how are you doing", "how's it going"):
            print("Chatbot: I'm doing great, thanks for asking! How about you?")

        # Added name response
        elif message in ("what is your name", "who are you", "what's your name"):
            print("Chatbot: I'm your friendly Python chatbot!")

        # Added help/capabilities response
        elif message in ("what can you do", "help"):
            print("Chatbot: I can chat with you, answer basic questions, and keep you company!")

        # Added gratitude response
        elif message in ("thanks", "thank you"):
            print(f"Chatbot: You're very welcome, {name}!")

        else:
            print("Chatbot: Sorry, I don't understand that yet. Try saying hello or asking who I am!")


if __name__ == "__main__":
    chatbot()