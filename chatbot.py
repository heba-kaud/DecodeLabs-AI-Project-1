print("🤖Hello! I am your AI Chatbot.")
print("Type 'bye' to exit")
while True:
    user_input = input("You:")
    if user_input.lower() in ["bye", "exit","goodbye", "quit"]:
        print("Bot: Goodbye!👋")
        break
    elif user_input.lower() == "hello":
        print("Bot: Hello!😊")
    elif user_input.lower() == "hi":
        print("Bot: Hi! how can i help you?🤖")
    elif user_input.lower().strip("?!.") in ["How are you?", "how r you", "how are u", "how are you", "are you okay?"]:
        print("Bot: I'm fine, thank you!😊")
    elif user_input.lower().strip("?!.") in ["what is your name?", "what's your name","your name"]:
        print("Bot: My name is AI Bot.🤖")
    elif user_input.lower().strip("?!.") == "what is ai?":
        print("Bot: Artifical Intelligance (AI) is the ability of machines to perform taskes that normally require human intelligence. ")
    elif user_input.lower().strip("?!.") == "is there a treatment for seborrheic dermatitis?":
        print("Bot: Yes, there are treatments that can help control seborrheic eczema. Treatment may include medicated shampoos or creams, depending on the affected area.")
    else:
        print("Bot: Sorry, I don't understand.🤔")
