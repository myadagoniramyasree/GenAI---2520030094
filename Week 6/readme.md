# Week 6 Skill – LLM Evaluation and Baseline Testing

## Overview
This skill focuses on evaluating the performance of a Large Language Model using a predefined Golden Question Set. The experiment uses the locally running Llama 3.2 model through Ollama to generate answers, compares them against expected answers using keyword-based scoring, and records the evaluation results in a CSV file.

The first evaluation is documented as **Release v0.1**.

## Objectives
- Create a Golden Question Set containing questions, expected answers, keywords, and source references.
- Run the Llama 3.2 model locally using Ollama.
- Generate responses for predefined questions.
- Evaluate generated answers using keyword-based scoring.
- Identify matched and missing keywords.
- Calculate the average keyword coverage.
- Store evaluation results in a CSV file.
- Establish the first baseline evaluation as Release v0.1.

## Technologies Used
- Python
- Ollama
- Llama 3.2
- Requests
- JSON
- CSV
- Visual Studio Code

## Project Structure
```text
Week 6 Skill/
│
├── golden_set.json
├── main.py
├── requirements.txt
├── baseline_results.csv
└── README.md
```

## Implementation

1. Verify the Ollama installation and download the Llama 3.2 model.
2. Create `golden_set.json` containing 30 questions, expected answers, keywords, and source URLs.
3. Configure the Ollama API endpoint and model name in `main.py`.
4. Implement a function to send questions to the Llama 3.2 model.
5. Generate answers using the Ollama API with temperature set to 0.
6. Implement keyword-based scoring to identify matched and missing keywords.
7. Assign PASS status for scores of 60% or above and REVIEW status for lower scores.
8. Store questions, expected answers, generated answers, scores, statuses, and sources in a CSV file.
9. Generate a baseline evaluation summary.
10. Label the first evaluation as Release v0.1.

## Execution

Install the required dependency:

```bash
pip install -r requirements.txt
```

Download the model if it is not already installed:

```bash
ollama pull llama3.2
```

Run the evaluation program:

```bash
python main.py
```

## Evaluation Process
The program evaluates each question in the Golden Question Set by:

- Sending the question to Llama 3.2.
- Generating an answer using the local model.
- Comparing the generated answer with the expected keywords.
- Calculating the keyword coverage percentage.
- Assigning PASS, REVIEW, or ERROR status.
- Saving the evaluation details in `baseline_results.csv`.

## Output Files

The program automatically generates:

**`baseline_results.csv`**

This file contains:
- Question ID
- Question
- Expected answer
- LLM-generated answer
- Matched keywords
- Missing keywords
- Evaluation score
- Evaluation status
- Source URL
- Model name
- Release version

## Expected Outcome
Successfully execute the first baseline evaluation of Llama 3.2 using a Golden Question Set of 30 questions, calculate keyword coverage, generate a CSV report, and document the experiment as Release v0.1.

## Key Concepts Covered
- Golden Question Set
- LLM evaluation
- Baseline testing
- Keyword-based scoring
- Answer comparison
- Evaluation metrics
- PASS and REVIEW classification
- CSV report generation
- Model evaluation and versioning

## Important Note
Keyword-based scoring measures keyword coverage and does not guarantee the factual correctness or quality of generated answers. The baseline results provide an initial reference for future model evaluation and improvements.
