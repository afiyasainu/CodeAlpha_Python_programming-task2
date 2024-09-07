import nltk
from nltk.chat.util import Chat, reflections

# Define pairs for conversation
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem!",]
    ],
    [
        r"I am fine",
        ["Great to hear!", "Awesome!",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
def chat():
    print("Hi! I am a chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    chat()
