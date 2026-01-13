def get_response(user_input):
    """
    Function to determine the chatbot's response based on user input.
    Uses if-elif statements to check for specific keywords.
    """
    user_input = user_input.lower().strip()
    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
    print("-" * 40)
    
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break

print("Chatbot session ended.")
