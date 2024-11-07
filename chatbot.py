''' My new project '''
''' This is a chatbot, i'm Working on '''

import random #allows it to choose random answers, prior to the user's input.
import datetime #This shows the current time and date

#This defines the chatbot responses
greetings = ["Hi!", "Hello!", "Hey!", "Whats up?", "Welcome!", "Hello there!", "Hafa na", "What can i help you with?"]
responses = ["I'm Fine and you", "I'm doing great, thanks!", "Good and you?"]
responses_2 = ["great!", "that's fine"]
goodbyes = ["Bye!", "See you later! ", "Goodbye!", "Have a nice day", "Take care"]
thanks = ["You are welcome!", " No problem!", "Thanks!", "Alright!", "Glad i could help!"]
jokes = ["why was the math book sad? Answer: Because it has too many problems hahaha.", "Why do programmers prefer dark mode? Answer: Because light attracts bugs hahaha.", "Why did the Wi-Fi router go to therapy?,Answer: Because it was feeling disconnected! hahaha"]
unknown = ["Sorry, i didn't get that.", "I'm not sure what you mean.", "Can you please rephrase that!"]

#This defines the chatbot functions
def greet(name):
    return f"{random.choice(greetings)} {name}!"

def response():
    return random.choice(responses)  

def response_2():
    return random.choice(responses_2)      

def date():
    return random.choice(dates)

def joke():
    return random.choice(jokes)    

def goodbye():
    return random.choice(goodbyes)

def thank():
    return random.choice(thanks)

def unknown_response():
    return random.choice(unknown)

def help():
    return "i can help with: \n1. Greetings \n2. Goodbyes \n3. Basic conversations \n4. Current Time \n5. Current Date \n6. Jokes"    

def current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")    

def current_date():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y")

#Chatbot loop
def chatbot():
    print("Chatbot: Hi!, what your name?")
    name = input("you: ")
    print("Chatbot:", greet(name))

    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "goodbye", "see you later"]:
            print("Chatbot:", goodbye())
            break
        elif user_input in ["hello","how are you", "how's it going", "i dey"]:
            print("Chatbot:", response())
        
        elif user_input in ["good", "okay then", "fine"]:
            print("Chatbot:", response_2())

        elif user_input in ["joke", "tell me a joke"]:
            print("Chatbot:", joke())            

        elif user_input in ["what's the time"]:
            print("Chatbot: The time is:",current_time())    

        elif user_input in ["what's today date"]:
            print("Chatbot: Today's date is:",current_date())

        elif user_input in ["thanks", "thank you"]:
            print("Chatbot:", thank())

        elif user_input in ["help", "what can you do"]:
            print("Chatbot:", help())

        elif user_input in ["what's your name"]:
            print("Chatbot: My name is Chatbot 2.0!")

        else:
            print("Chatbot:", unknown_response())
        
#this is to run the chatbot
chatbot()