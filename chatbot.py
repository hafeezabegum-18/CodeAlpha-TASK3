
def chatbot():
    print("="*20)
    print("Welcome to the CHATBOT 🤖")
    print("="*20) 

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["exit", "quit", "bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break

    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Chatbot: Hello! How can I assist you?")

    elif "how are you" in user_input:
        print("Chatbot:  I'm doing great! How about you?")

    elif "what is your name" in user_input or "explain about yourself" in user_input:
        print("Chatbot: I am a simple chatbot created to assist you.")

    elif "what can you do" in user_input or "help" in user_input:
        print("Chatbot: I can chat with you, answer simple questions, and provide assistance.")

    elif "do you have any feelings" in user_input or "are you human" in user_input:
        print("Chatbot: I am a program, so I don't have feelings, but I'm here to help!")

    else:
        print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
