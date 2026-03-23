responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "good morning": "Good morning!",
    "good evening": "Good evening!",
    "how are you":"I'm fine!",
    "your name": "I am your chatbot!",
    "what can you do": "I can chat with you!",
    "bye": "Goodbye! Have a nice day!"
}

print("Bot: Hello! I am your chatbot.")
print("You can say things like: hello, hi, how are you, your name, bye")

while True:
    user_input = input("You: ").lower().strip()

    if any(word in user_input for word in["hi", "hello", "hey"]): 
        print("Bot: Hello!")
        continue

    reply = responses.get(user_input, "I'm still learning. Try something else!")
    print("Bot:", reply)

    if user_input == "bye":
        break

        