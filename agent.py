from baml_client import b
from tools.symsolver import quadratic_equation_solver, quadratic_derivative, evaluate_equation
from typing import Dict, Any, List, Union
from baml_client.types import QuandraticSolver, QuadraticDerivative, QuadraticEvaluator, MessageToUser
from baml_py import Collector

class Agent:
    """
    Agent class that handles user interactions and tool calls.
    
    This agent processes user messages, calls the appropriate LLM or tools,
    and maintains conversation history for context in future interactions.
    """
    
    def __init__(self, context_trimming: bool = True):
        """
        Initialize the agent with an empty message history.
        
        Args:
            context_trimming: Flag to control streaming behavior. Default is True.
        """
        self.message_history: List[Dict[str, Any]] = []
        self.context_trimming: bool = context_trimming
        self.metrics_collector = Collector(name="metrics-collector")

        
    def use_tool(self, agent_response) -> Dict[str, Any]:
        """
        Process the agent response and use the appropriate tool based on the tool type.
        
        Args:
            agent_response: The response from the BAML MathChat
            
        Returns:
            A dictionary containing the tool response
        """
        # If context_trimming is enabled, we may need to summarize context
        # or append tool responses based on task status
        # Handle different tool types using the union pattern
        tools = agent_response.tools
        
        if isinstance(tools, MessageToUser):
            # Direct message to user
            tool_response = {
                'role': 'assistant',
                'msg': tools.response,
                'tool_name': 'message_to_user',
                'metadata': {
                    'task_status': tools.task_status
                }
            }
            # For message_to_user, the agent response is the same as the tool response
            self.message_history.append(tool_response)
            
            # If context trimming is enabled and task status is completed,
            # pass message history to summarize context BAML function
            if self.context_trimming and tools.task_status == "COMPLETED":
                
                # Convert message history to string list for BAML function
                message_history_str = [str(message) for message in self.message_history]
                
                # Call SummarizeContext BAML function
                summarized_context = b.SummarizeContext(message_history_str)
                
                # Replace message history with summarized context
                self.message_history = summarized_context
               
                
            return tool_response
        
        elif isinstance(tools, QuandraticSolver):
            # Add agent response to message history
            self.message_history.append({
                'role': 'assistant',
                'msg': 'I need to solve this quadratic equation',
                'tool_name': 'quadratic_solver',
                'tool_args': {
                    'equation': tools.equation
                }
            })
            
            # Call quadratic equation solver
            equation = tools.equation
            print(f"🧮 Calling quadratic equation solver tool with equation: {equation}")
            result = quadratic_equation_solver(equation)
            
            # Format tool response
            tool_response = {
                'role': 'tool',
                'msg': f"Solved equation: {equation}. Roots: {result}",
                'tool_name': 'quadratic_solver',
                'metadata': {
                    'equation': equation,
                    'result': str(result),
                    'task_status': 'COMPLETED'  # Assuming tool execution completes the task
                }
            }
            

            self.message_history.append(tool_response)
                
            return tool_response
            
        elif isinstance(tools, QuadraticDerivative):
            # Add agent response to message history
            self.message_history.append({
                'role': 'assistant',
                'msg': 'I need to find the derivative of this quadratic equation',
                'tool_name': 'quadratic_derivative',
                'tool_args': {
                    'equation': tools.equation
                }
            })
            
            # Call quadratic derivative function
            equation = tools.equation
            print(f"📈 Calling quadratic derivative tool with equation: {equation}")
            result = quadratic_derivative(equation)
            
            # Format tool response
            tool_response = {
                'role': 'tool',
                'msg': f"Derivative of equation: {equation}. Result: {result}",
                'tool_name': 'quadratic_derivative',
                'metadata': {
                    'equation': equation,
                    'result': str(result),
                    'task_status': 'COMPLETED'  # Assuming tool execution completes the task
                }
            }
            
            self.message_history.append(tool_response)
                
            return tool_response
            
        elif isinstance(tools, QuadraticEvaluator):
            # Add agent response to message history
            self.message_history.append({
                'role': 'assistant',
                'msg': 'I need to evaluate this quadratic equation at a specific x value',
                'tool_name': 'quadratic_evaluator',
                'tool_args': {
                    'equation': tools.equation,
                    'x_value': tools.x_value
                }
            })
            
            # Call quadratic evaluator function
            equation = tools.equation
            x_value = tools.x_value
            print(f"🔢 Calling quadratic evaluator tool with equation: {equation} at x = {x_value}")
            result = evaluate_equation(equation, float(x_value))
            
            # Format tool response
            tool_response = {
                'role': 'tool',
                'msg': f"Evaluated equation: {equation} at x = {x_value}. Result: {result}",
                'tool_name': 'quadratic_evaluator',
                'metadata': {
                    'equation': equation,
                    'x_value': x_value,
                    'result': str(result),
                    'task_status': 'COMPLETED'  # Assuming tool execution completes the task
                }
            }
            
            self.message_history.append(tool_response)
                
            return tool_response
            
        else:
            # Handle unknown tool type
            error_message = f"Unknown tool type: {type(tools)}"
            print(f"❓ Unknown tool type requested: {type(tools)}")
            raise Exception(error_message)
    
    def chat(self, user_message: str) -> str:
        """
        Process a user message and return a response.
        
        Args:
            user_message: The message from the user
            
        Returns:
            A string response to the user
        """
        # Add user message to history
        self.message_history.append({
            'role': 'user',
            'msg': user_message
        })
        
        while True:
            # Get response from BAML MathChat
            agent_response = b.MathChat([str(message) for message in self.message_history], baml_options={"collector": self.metrics_collector})
            
            # Use the tool and get the response
            tool_response = self.use_tool(agent_response)
                   
            # If it's a direct message to the user, return it
            if tool_response['role'] == 'assistant':
                return tool_response['msg']
            
            
    def metrics(self):
        return self.metrics_collector.usage
