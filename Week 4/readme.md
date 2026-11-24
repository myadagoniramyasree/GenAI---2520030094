# Week 4 Skill – Comparison of BPE, WordPiece and SentencePiece Tokenizers

## Overview
This skill focuses on implementing and comparing three subword tokenization approaches: Byte Pair Encoding (BPE), WordPiece, and SentencePiece. The experiment uses pretrained tokenizers to process English, Telugu, and Hindi text and examines how each tokenizer splits sentences into tokens and generates token IDs.

## Objectives
- Understand why tokenization is required before text is processed by a language model.
- Observe the difference between word-level and subword-level tokenization.
- Implement pretrained BPE, WordPiece, and SentencePiece tokenizers.
- Compare token pieces and token counts for English, Telugu, and Hindi.
- Understand why token counts differ across tokenizer vocabularies and training data.

## Technologies Used
- Python
- Hugging Face Transformers
- SentencePiece
- GPT-2
- Multilingual BERT
- XLM-RoBERTa
- Visual Studio Code

## Tokenizers Used

| Tokenization Approach | Pretrained Model |
|---|---|
| BPE | GPT-2 |
| WordPiece | bert-base-multilingual-cased |
| SentencePiece | xlm-roberta-base |

## Project Structure
```text
Week 4 Skill/
│
├── requirements.txt
├── tokenizer_comparison.py
└── README.md
```

## Implementation
1. Set up the Python environment in Visual Studio Code.
2. Install the required libraries using `requirements.txt`.
3. Import `AutoTokenizer` from the Transformers library.
4. Load the pretrained GPT-2, Multilingual BERT, and XLM-R tokenizers.
5. Provide sample text in English, Telugu, and Hindi.
6. Encode each sentence using all three tokenizers.
7. Extract the token pieces and their corresponding token IDs.
8. Display and compare the token counts for each language.

## Execution

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Python program:

```bash
python tokenizer_comparison.py
```

The program loads the pretrained tokenizers and displays their token pieces, token IDs, and token counts for each language.

## Expected Outcome
Successfully implement and compare BPE, WordPiece, and SentencePiece tokenizers using English, Telugu, and Hindi text. Observe how different tokenizer vocabularies and training data influence token splitting and token counts.

## Key Concepts Covered
- Natural Language Processing (NLP)
- Text tokenization
- Word-level and subword-level tokenization
- Byte Pair Encoding (BPE)
- WordPiece
- SentencePiece
- Token IDs
- Multilingual tokenization
