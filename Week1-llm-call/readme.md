# Week 1 Skill – First LLM API Call Using Python

## Overview
This skill demonstrates how to connect a Python application to a Large Language Model (LLM) using an API. It focuses on making the first LLM API call, securely managing API keys, and generating AI-powered responses through Python.

## Objectives
- Understand the role of API keys in connecting applications to LLMs.
- Install and use the required Python libraries.
- Store API keys securely using environment variables and a `.env` file.
- Connect a Python application to an LLM API.
- Send prompts and display AI-generated responses.
- Identify and troubleshoot common API errors.

## Technologies Used
- Python
- OpenAI Python SDK
- Google Gemini SDK (alternative implementation)
- python-dotenv
- Visual Studio Code

## Project Structure
```text
Week 1 Skill/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Implementation
1. Set up the Python environment in Visual Studio Code.
2. Install the required dependencies using `requirements.txt`.
3. Create a `.env` file to store the API key securely.
4. Configure `.gitignore` to prevent sensitive files from being uploaded.
5. Develop `main.py` to initialize the LLM client.
6. Send a prompt to the selected AI model.
7. Display the generated response in the terminal.

## Execution
Run the application using:

```bash
python main.py
```

The program sends a prompt to the configured LLM and displays its generated response in the terminal.

## Expected Outcome
Successfully establish a connection between a Python application and an LLM API, submit a prompt, and receive an AI-generated response.

## Key Learnings
- Understanding LLM API integration.
- Secure API key handling.
- Working with Python SDKs.
- Prompt submission and response generation.
- Basic API error handling and troubleshooting.

## Security Note
API keys and other sensitive credentials must never be uploaded to GitHub. The `.env` file should be excluded using `.gitignore`.
