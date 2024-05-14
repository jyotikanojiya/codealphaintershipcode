import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ["my name is (.*)", ["Hello %1, how can I help you today?"]],
    ["(what is your name?|who are you?)", ["I am a basic chatbot."]],
    ["(how are you?|how's it going?)", ["I'm doing well, thank you!"]],
    ["(.) (weather|temperature) (.)", ["I'm sorry, I'm not equipped to provide weather updates."]],
    ["(.*)", ["Sorry, I didn't understand that."]]
]

# Create a Chatbot
chatbot = Chat(pairs, reflections)

# Define a function to interact with the chatbot
def chat():
    print("Hello! I'm a basic chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if user_input.lower() == 'exit':
            break

# Start the conversation
chat()