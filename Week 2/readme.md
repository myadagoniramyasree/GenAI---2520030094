# Week 2 Skill – Provider-Agnostic LLM Client

## Overview
This skill focuses on building a provider-agnostic Large Language Model (LLM) client that supports both hosted cloud APIs and locally running language models. A common interface is developed to interact with different LLM providers without changing the overall application logic.

## Objectives
- Understand the concept of provider-agnostic LLM integration.
- Create a common interface for different LLM providers.
- Connect to Google Gemini as a hosted LLM provider.
- Run Llama 3.2 locally using Ollama.
- Generate responses through a common LLM client.
- Perform unit testing using Python's unittest framework.

## Technologies Used
- Python
- Google Gemini API
- Ollama
- Llama 3.2
- Requests
- python-dotenv
- unittest
- Visual Studio Code

## Project Structure
```text
Week 2 Skill/
│
├── .env
├── llm_client.py
├── main.py
├── test_client.py
├── requirements.txt
└── README.md
```

## Implementation
1. Download and install Ollama on the local system.
2. Download the Llama 3.2 model using `ollama pull llama3.2`.
3. Create the required Python project files.
4. Define a common `LLMProvider` interface.
5. Implement `GeminiProvider` for cloud-based LLM access.
6. Implement `OllamaProvider` for local model execution.
7. Develop the `LLMClient` class to interact with either provider.
8. Create `main.py` to select the provider and generate responses.
9. Write unit tests to verify the common client functionality.

## Execution

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Choose the provider when prompted:
- `gemini` – Uses the hosted Google Gemini API.
- `ollama` – Uses the locally installed Llama 3.2 model.

Enter a question to receive the generated response.

## Testing
Run the unit tests using:

```bash
python -m unittest test_client.py
```

The test verifies that the common LLM client correctly passes a prompt to a provider and returns the expected response.

## Expected Outcome
Successfully build and execute a single LLM client interface that supports both cloud-based and locally hosted language models.

## Key Learnings
- Provider-agnostic architecture.
- Abstract classes and common interfaces in Python.
- Integration of cloud-based and local LLM providers.
- Running local language models using Ollama.
- Environment variable management.
- Unit testing with Python's unittest framework.

## Security Note
Store API keys in the `.env` file and never expose them in public repositories or screenshots.
