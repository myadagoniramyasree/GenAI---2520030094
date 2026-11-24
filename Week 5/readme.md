# Week 5 Skill – Token Economics: Cost and Rate-Limit Budgeting

## Overview
This skill focuses on estimating token consumption, API costs, 
and rate-limit requirements before developing an LLM-powered feature. A Python-based budgeting tool is developed to calculate expected input and output tokens, 
estimate daily and monthly costs, check RPM and TPM limits, and generate a go/no-go recommendation based on configured budgets.

## Objectives
- Understand input tokens, output tokens, and total tokens.
- Understand Requests Per Minute (RPM) and Tokens Per Minute (TPM).
- Estimate daily and monthly token consumption.
- Calculate hosted API costs using configurable token prices.
- Check expected traffic against RPM and TPM limits.
- Apply a safety margin to usage and cost estimates.
- Identify risky assumptions using budget thresholds and automated tests.

## Technologies Used
- Python
- python-dotenv
- unittest
- Visual Studio Code

## Project Structure
```text
Week 5 Skill/
│
├── .env
├── budget.py
├── test_budget.py
├── requirements.txt
└── README.md
```

## Implementation
1. Create the project folder and required Python files.
2. Configure token prices, expected requests, token usage, rate limits, and budget thresholds in `.env`.
3. Create a `FeatureBudget` class to manage feature assumptions.
4. Implement calculations for daily token consumption and estimated API costs.
5. Calculate monthly cost based on a 30-day estimate.
6. Apply a safety margin to forecast usage and costs.
7. Check RPM, TPM, daily budget, and monthly budget limits.
8. Generate a token economics report with PASS or REVIEW status.
9. Create automated unit tests to verify cost calculations and capacity checks.

## Execution

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the budget planner:

```bash
python budget.py
```

Run the automated tests:

```bash
python -m unittest test_budget.py
```

## Sample Output

Using the illustrative assumptions provided in the practical:

| Metric | Expected Value |
|---|---:|
| Input tokens/day | 2,400,000 |
| Output tokens/day | 600,000 |
| Total tokens/day | 3,000,000 |
| Estimated daily cost | $1.44 |
| Estimated monthly cost | $43.20 |
| Peak RPM with margin | 36 |
| Peak TPM with margin | 54,000 |

The program also displays PASS or REVIEW for RPM capacity, TPM capacity, daily budget, and monthly budget.

## What-If Analysis
The planner can be tested by changing one assumption at a time:

- Increase daily requests to observe changes in token consumption and cost.
- Increase peak RPM to test rate-limit capacity.
- Increase input tokens to observe input cost and TPM changes.
- Reduce output tokens to understand cost savings.
- Increase token prices to evaluate a higher-priced model.
- Reduce repeated model calls through caching to lower cost and rate-limit pressure.
  
## Key Concepts Covered
- Token budgeting
- Input and output token estimation
- API cost estimation
- Requests Per Minute (RPM)
- Tokens Per Minute (TPM)
- Safety margin
- Daily and monthly budget thresholds
- What-if analysis
- Pre-build go/no-go decisions
- Automated unit testing
  
## Expected Outcome
Successfully develop a reusable Python-based token budgeting tool that estimates LLM usage and costs, 
checks configured rate limits and budget thresholds, and provides a go/no-go recommendation before implementing an LLM-powered feature.
