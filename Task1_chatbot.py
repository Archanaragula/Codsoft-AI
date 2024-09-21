# Simple AI-based Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for better matching

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    # Ask for name
    elif "what is your name" in user_input or "who are you" in user_input:
        return "I'm your friendly chatbot! You can call me ChatBot."
    
    # Basic inquiries
    elif "how are you" in user_input:
        return "I'm doing well, thank you! How about you?"
    
    # Help inquiry
    elif "help" in user_input or "assist" in user_input:
        return "Sure! I can help you with basic queries. What do you need assistance with?"
    
    # Farewell
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Rule for asking about AI
    elif "what is ai" in user_input or "artificial intelligence" in user_input:
        return "AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think and learn."
    
    # Small talk
    elif "what's your favorite color" in user_input:
        return "I don't have eyes, but if I did, I think I'd like blue!"
    
    # Rule for unknown queries
    else:
        return "I'm not sure how to respond to that. Can you please ask something else?"

# Running the chatbot in a loop to simulate conversation
def start_chatbot():
    print("ChatBot: Hello! I'm your chatbot. Type 'bye' to end the chat.")
    
    while True:
        user_input = input("You: ")  # Get user input
        
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        # Generate and print chatbot response
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
