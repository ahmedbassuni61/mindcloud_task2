Commands={
    "hi": "Hello!",
    "how are you": "I'm fine, thank you"
}

user_name = None

print("Chatbot: Hello! What's your name?")
while True:
    user_input = input("You: ").strip().lower()
    # Save name if not set
    if not user_name:
        user_name = user_input.capitalize()
        print(f"Chatbot: Nice to meet you, {user_name}!")
        print("Chatbot: You Can say 'hi' 'how are you' 'add' 'sub' 'exit'")
        continue

    
    # Simple addition
    if user_input=="add":
        print("Chatbot: Type two numbers with a space in between")
        try:
            values = input().split()
            a = int(values[0])
            b = int(values[1])
            result=a+b
            print(f"Chatbot: Result is {result}")
        except:
            print("Try again")
        continue
    
    # Simple subtraction
    if user_input=="sub":
        print("Chatbot: Type two numbers with a space in between")
        try:
            values = input().split()
            a = int(values[0])
            b = int(values[1])
            result=a-b
            print(f"Chatbot: Result is {result}")
        except:
            print("Try again")
        continue
    
    # Answer from knowledge
    if user_input in Commands:
        print(f"Chatbot: {Commands[user_input]}")
    else:
        print("Chatbot: Sorry, I don't know that yet.")

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
