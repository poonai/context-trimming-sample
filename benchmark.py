
from agent import Agent
import json
from dotenv import load_dotenv

load_dotenv()  # take environment variables


QUESTIONS = [
  "Solve the quadratic equation: x^2 + 5*x + 6 = 0",
  "Find the derivative of: 2*x^2 + 4*x - 6 ",
  "what is the square of the roots",
]

def run_benchmark():
    """
    Run the benchmark comparing agents with and without context trimming.
    
    This function creates two agent instances, passes the same
    questions to each, and prints the usage statistics at the end.
    """

    print("\n=== Starting Benchmark ===\n")
    
    # Initialize agents
    smart_agent = Agent(context_trimming=True)  # Agent with context trimming
    agent = Agent(context_trimming=False)       # Agent without context trimming
    
    # Process each question with both agents
    for i, question in enumerate(QUESTIONS):
        print(f"\nQuestion {i+1}: {question}")
        
        print("\n--- Smart Agent (with context trimming) Response ---")
        smart_response = smart_agent.chat(question)
        print(smart_response)
        
        print("\n--- Agent (without context trimming) Response ---")
        regular_response = agent.chat(question)
        print(regular_response)
    
    # Get and print usage statistics
    smart_usage = smart_agent.metrics()
    regular_usage = agent.metrics()
    
    print("\n=== Benchmark Results ===\n")
    
    print("Smart Agent (with context trimming):")
    print(smart_usage)
    
    print("\nAgent (without context trimming):")
    print(regular_usage)


if __name__ == "__main__":
    run_benchmark()
