from agent import Agent
import sys
from dotenv import load_dotenv

load_dotenv()  # take environment variables

def main():
    """
    Main function that runs an interactive chat session with the math agent.
    
    This function creates an instance of the Agent class and allows users to
    interact with it through the command line interface.
    """
    print("=== Math Agent Interactive Chat ===")
    print("Type 'exit', 'quit', or 'q' to end the session")
    print("Type 'help' for information about available capabilities")
    print("=" * 36)
    
    # Initialize the agent
    agent = Agent()
    
    # Help message
    help_message = """
Available capabilities:
- Solve quadratic equations (e.g., "Solve x^2 - 5x + 6 = 0")
- Find derivatives of quadratic equations (e.g., "What is the derivative of 2x^2 + 4x - 6?")
- Evaluate quadratic equations (e.g., "Evaluate 3x^2 - 2x + 1 when x = 2")
- Ask general math questions
    """
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
                
            # Check for help command
            if user_input.lower() == 'help':
                print(help_message)
                continue
                
            # Skip empty inputs
            if not user_input:
                continue
                
            # Process the user input and get response
            response = agent.chat(user_input)
            
            # Display the response
            print(f"\nAgent: {response}")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nSession terminated by user. Goodbye!")
            break
            
        except Exception as e:
            # Handle any unexpected errors
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again or type 'exit' to quit.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)
