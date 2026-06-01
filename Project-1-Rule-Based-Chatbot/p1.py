# Rule-Based AI Chatbot

# Dictionary of responses
responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 👋",
    "hey": "Hey! 😊",
    "hii": "Hi! 😄",

    "how are you": "I am doing great!",
    "how r u": "I'm fine 😄",
    "how are u": "Doing well!",

    "what is your name": "I am a simple AI chatbot 🤖",
    "your name": "I am Janusha's AI chatbot 😄",

    "thanks": "You're welcome!",
    "thank you": "Happy to help 😊",

    "bye": "Goodbye! 👋",
    "goodbye": "See you later!",
    "see you": "Take care 😄"
}

print("AI Chatbot Started!")
print("Type 'exit' to stop the chatbot.\n")

# Infinite loop
while True:

    # User input
    user_input = input("You: ")

    # Input sanitization
    clean_input = user_input.lower().strip()

    # Exit condition
    if clean_input == "exit":
        print("Bot: Chat ended. Goodbye!")
        break

    # Get response from dictionary
    response = responses.get(
        clean_input,
        "Sorry, I don't understand that."
    )

    # Print response
    print("Bot:", response)
