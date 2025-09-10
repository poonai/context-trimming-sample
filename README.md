# Math Agent

A mathematical agent that solves equations which require stitching multiple tool results. This is a sample code for the blog post [Context Pruning in Conversational Agents](https://poonai.xyz/posts/context-pruning-in-conversational-agent/).

## Features

- Solve quadratic equations (e.g., "Solve x^2 - 5*x + 6 = 0")
- Find derivatives of quadratic equations (e.g., "What is the derivative of 2x^2 + 4*x - 6?")
- Evaluate quadratic equations at specific x values (e.g., "Evaluate 3x^2 - 2*x + 1 when x = 2")
- Answer general math questions
- Context trimming to reduce token usage in conversations

## Installation

This project uses [UV](https://github.com/astral-sh/uv) for dependency management. UV is a modern Python package installer and resolver.

1. Clone the repository:
   ```bash
   git clone https://github.com/poonai/context-trimming-sample.git
   cd math-agent
   ```

2. Install dependencies using UV:
   ```bash
   uv sync
   ```

## Configuration

Create a `.env` file in the root directory with your OpenRouter API key:

```
OPENROUTER_API_KEY="your-api-key-here"
```

You can get an API key from [OpenRouter](https://openrouter.ai/).

## Usage

### Interactive Chat

Run the agent in interactive mode to chat with it:

```bash
python main.py
```

This will start an interactive chat session where you can ask the agent to solve quadratic equations, find derivatives, and more.

Example commands:
- `Solve x^2 - 5x + 6 = 0`
- `What is the derivative of 2x^2 + 4x - 6?`
- `Evaluate 3x^2 - 2x + 1 when x = 2`
- Type `help` to see available capabilities
- Type `exit`, `quit`, or `q` to end the session

### Benchmark

Run the benchmark to compare agents with and without context trimming:

```bash
python benchmark.py
```