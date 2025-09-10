
class QuandraticSolver {

    type "quadratic_solver" @description(#"
        DESCRIPTON: QuandraticSolver is used to solve quadratic equation
    "#)

    equation string @description(#"
        eg: 2*x^2 + 4*x - 6 = 0
    "#)
}

class QuadraticDerivative {
    type "quadratic_derivative" @description(#"
        DESCRIPTION: QuadraticDerivative is used to find the derivative of quadratic equation
    "#)

    equation string @description(#"
        eg: 2*x^2 + 4*x - 6 = 0
    "#)
}

class QuadraticEvaluator {
    type "quadratic_evaluator" @description(#"
         DESCRIPTION: QuadraticEvaluator is used to evaluate an quadratic equation
    "#)

    equation string @description(#"
        eg: 2*x^2 + 4*x - 6 = 0
    "#)

    x_value string @description(#"
        The value to substitute for x
    "#)
}

enum TaskStatus {
    COMPLETED 
    PROCESSING
}

class MessageToUser {
    type "message_to_user" @description(#"
        DESCRIPTION: MessageToUser is used to respond to the user
    "#)

    response string @description(#"
        The assitant response to the user
    "#)

    task_status TaskStatus
}


class AgentResponse {
    tools QuandraticSolver  | QuadraticDerivative | QuadraticEvaluator | MessageToUser
}

function MathChat(message_history: string[]) -> AgentResponse {
    client OpenRouter
    prompt #"
        You're an helpful Math AI assistant. You have tools to solve equation related to quadratic 
        equation. The user query could be simple ,or complex that requires you to take mutiples turns
        between you and tools to resolve user query.

        Use message_to_user tools to reply or ask clarification question to the user.

        <CONVERSATION HISTORY>
        {% for message in message_history %}
         {{ message}}  
        {% endfor %}
        </CONVERSATION HISTORY>
       
        {{ctx.output_format}}
    "#
}

function SummarizeContext(message_history: string[]) -> string []{
    client OpenRouter
    prompt #"
         Your job is to summerize the user conversation to reduce the token length.
         ideas to summerize:
         - remove intermediate tool call and tool response 
         - summerize the user question and response in concise form

         <EXAMPLE INPUT>
           {'role': 'user', 'msg': 'solve x^2 - 5*x + 6 =0 and find derivative'}  
           {'role': 'assistant', 'msg': 'I need to solve this quadratic equation', 'tool_name': 'quadratic_solver', 'tool_args': {'equation': 'x^2 - 5*x + 6 = 0'}}  
           {'role': 'tool', 'msg': 'Solved equation: x^2 - 5*x + 6 = 0. Roots: [2, 3]', 'tool_name': 'quadratic_solver', 'metadata': {'equation': 'x^2 - 5*x + 6 = 0', 'result': '[2, 3]'}}  
           {'role': 'assistant', 'msg': 'I need to find the derivative of this quadratic equation', 'tool_name': 'quadratic_derivative', 'tool_args': {'equation': 'x^2 - 5*x + 6 = 0'}}  
           {'role': 'tool', 'msg': 'Derivative of equation: x^2 - 5*x + 6 = 0. Result: 2*x - 5', 'tool_name': 'quadratic_derivative', 'metadata': {'equation': 'x^2 - 5*x + 6 = 0', 'result': '2*x - 5'}}
           {'role': 'assistant', 'msg': 'The roots of the equation x^2 - 5*x + 6 = 0 are 2 and 3. The derivative of the equation is 2*x - 5. If you want me to evaluate the equation or the derivative at a specific x value, please let me know.', 'tool_name': 'message_to_user'}    
         </EXAMPLE INPUT>

        <EXAMPLE OUTPUT>
           {'role': 'user', 'msg': 'solve x^2 - 5*x + 6 =0 and find derivative'}  
           {'role': 'assistant', 'msg': 'The roots of the equation x^2 - 5*x + 6 = 0 are 2 and 3. The derivative of the equation is 2*x - 5. 'tool_name': 'message_to_user'}    
        </EXAMPLE OUTPUT>

        <BAD OUTPUT>
          "User asked to solve x^2 - 5*x + 6 = 0, find its derivative, and the squares of the roots; assistant provided roots (2, 3), derivative (2*x - 5), and squares (4, 9)."
        </BAD OUTPUT>

        <GOOD OUTPUT>
        {'role': 'user', 'msg': 'solve x^2 - 5*x + 6 =0 and find derivative'}
        {'role': 'assistant', 'msg': 'roots (2, 3), derivative (2*x - 5), and squares (4, 9). 'tool_name': 'message_to_user'} 
        </GOOD OUTPUT>
        
        <INPUT>
        {% for message in message_history %}
         {{ message}}  
        {% endfor %}
        </INPUT>
        {{ctx.output_format}}
    "#
} 