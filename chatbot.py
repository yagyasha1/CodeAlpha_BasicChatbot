
# CodeAlpha Task 4: Basic Chatbot

def chatbot():

    print("=" * 40)
    print("       WELCOME TO MY CHATBOT")
    print("=" * 40)

    print("Bot: Hello! I am your Python chatbot.")
    print("Bot: Type 'bye' to end the conversation.")

    conversation_count = 0

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input == "":
            print("Bot: Please type something.")
            continue

        conversation_count += 1

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user_input in ["what is your name", "your name"]:
            print("Bot: I am CodeAlpha's Python chatbot.")

        elif user_input == "what can you do":
            print("Bot: I can answer simple predefined questions.")

        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")

        elif user_input == "help":
            print("Bot: Try saying hello, how are you, or what is your name.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

    print("\nTotal messages received:", conversation_count)
    print("Thank you for chatting!")

# Start chatbot
chatbot()

