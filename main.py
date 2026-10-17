
def chatbot():
    print("Welcome to the Basic Chatbot!")
    print("Type 'help' to see what I can ask.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hi! How can I help you?")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input in ["what is your name", "your name"]:
            print("Bot: My name is Python Chatbot.")
        elif user_input == "help":
            print("Bot: Say hello, ask how I am, or type bye to exit.")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
