# Week 3 Skill – LLM Monitoring with MongoDB

## Overview
This skill extends the provider-agnostic LLM client developed in Week 2 by introducing usage monitoring and database logging. It captures token consumption, response latency, and estimated API costs for every LLM request and stores the records in MongoDB. It also implements request timeouts and retry mechanisms to improve reliability.

## Objectives
- Capture input and output token usage from Gemini and Ollama.
- Measure the response latency of each LLM request.
- Estimate hosted API costs using configurable token rates.
- Store successful and failed request details in MongoDB.
- Implement request timeouts and retry handling for temporary failures.

## Technologies Used
- Python
- Google Gemini API
- Ollama (Llama 3.2)
- MongoDB Atlas
- PyMongo
- Requests
- python-dotenv
- unittest

## Project Structure
```text
Week 3/
│
├── .env
├── main.py
├── llm_client.py
├── usage_logger.py
├── test_client.py
├── requirements.txt
└── README.md
```

## Implementation
1. Install the required Python dependencies.
2. Configure the Gemini API key and MongoDB connection string in the `.env` file.
3. Create a MongoDB Atlas cluster and configure database access.
4. Develop `usage_logger.py` to connect to MongoDB and store usage records.
5. Update `llm_client.py` to capture token usage, measure latency, and estimate API costs.
6. Implement timeouts and retry handling for temporary errors.
7. Update `main.py` to select Gemini or Ollama as the LLM provider.
8. Create unit tests using a fake provider and logger.
9. Verify that request details are successfully stored in MongoDB.

## Execution

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the unit tests:

```bash
python -m unittest test_client.py
```

Run the application:

```bash
python main.py
```

Choose the provider:
- `gemini` – Uses the hosted Google Gemini API.
- `ollama` – Uses the locally running Llama 3.2 model.

Enter a prompt to generate a response and record its usage details.

## MongoDB Logging
The application stores usage records in:

- **Database:** `llm_monitoring`
- **Collection:** `api_usage`

Each record includes provider, model, input tokens, output tokens, total tokens, latency, estimated cost, request status, number of attempts, and timestamp. Failed requests also include error details.

## Key Concepts Covered
- Token usage tracking
- Response latency monitoring
- API cost estimation
- MongoDB database integration
- Request timeouts
- Retry mechanisms with exponential delays
- LLM observability and reliability

## Expected Outcome
Successfully extend the LLM client with monitoring capabilities and store request usage information in MongoDB Atlas for tracking model performance, token consumption, estimated costs, and reliability.

## Security Note
Store API keys and MongoDB connection strings in `.env`. Never upload credentials or sensitive connection details to GitHub.
