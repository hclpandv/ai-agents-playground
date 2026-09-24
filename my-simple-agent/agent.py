'''
This is a simple agent that uses the Ollama model to perform tasks based on user input.
The agent can get the current time, save content to a file, and read content from a file.
This uses pydantic-ai to define the agent, model, and tools.
'''
import os
import dotenv
from datetime import datetime

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

# Load environment variables
dotenv.load_dotenv()

# Define the model and provider using environment variables
##

model = OllamaModel(
    model_name=os.environ.get("OLLAMA_MODEL_NAME"),
    provider=OllamaProvider(base_url=os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1")),
)

## tools to be used by agent

def get_current_time() -> str:
    """Returns the current time as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_file(filename: str, content: str) -> str:
    """Saves the given content to a file and returns a confirmation message."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Content saved to {filename}"

def read_from_file(filename: str) -> str:
    """Reads content from a file and returns it."""
    with open(filename, "r") as f:
        return f.read() 

# Agent that uses the model and tools defined above
##
agent = Agent(
    model=model,
    tools=[
        get_current_time,
        save_to_file,
        read_from_file,
    ],
    instructions="You are a helpful assistant that can use the provided tools to perform the actions when requested."
)

def main():
    print("Welcome to the Simple Agent!")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the agent. Goodbye!")
            break

        result = agent.run_sync(user_input)
        print(f"Agent: {result.output}")

if __name__ == "__main__":
    main()
