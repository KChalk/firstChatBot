#built from  https://towardsdatascience.com/build-your-first-chatbot-using-python-nltk-5d07b027e727
from nltk.chat.util import Chat, reflections

from pairs import init_replies

initial_replies = init_replies()

def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(initial_replies, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()
    # who are you -- > Brad Pitt
    