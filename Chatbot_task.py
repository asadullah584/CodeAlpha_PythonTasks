"""
Simple Rule-Based Chatbot
-------------------------
A beginner-friendly chatbot that replies to user input using
predefined rules (if-elif conditions).

Key Concepts Used:
    - if-elif-else statements
    - Functions
    - Loops (while)
    - Input / Output
"""


def get_response(user_input):
    """
    Return a predefined reply based on the user's message.

    Parameters:
        user_input (str): The message typed by the user.

    Returns:
        str: The chatbot's reply.
    """
    # Normalize input: remove extra spaces and convert to lowercase
    # so "Hello", "HELLO" and " hello " are all treated the same.
    message = user_input.strip().lower()

    # Rule-based conditions
    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("what is your name", "who are you"):
        return "I'm a simple rule-based chatbot."
    elif message in ("help", "what can you do"):
        return "I can reply to: hello, how are you, what is your name, bye."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        # Default reply when no rule matches
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def chatbot():
    """
    Run the chatbot in a loop until the user says goodbye.
    """
    print("=" * 45)
    print("        Welcome to the Simple Chatbot")
    print("   Type 'bye' to exit | Type 'help' for tips")
    print("=" * 45)

    # Loop keeps the conversation going until an exit word is entered
    while True:
        user_input = input("You: ")

        # Ignore empty input and ask again
        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        # Get the reply from the rule-based function
        reply = get_response(user_input)
        print("Bot:", reply)

        # Stop the loop if the user wants to leave
        if user_input.strip().lower() in ("bye", "goodbye", "exit"):
            break


# Entry point: runs the chatbot only when this file is executed directly
if __name__ == "__main__":
    chatbot()