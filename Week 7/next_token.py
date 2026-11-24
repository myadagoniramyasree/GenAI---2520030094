
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 1: Load a small pretrained open model
MODEL_NAME = "distilgpt2"

print("Loading model:", MODEL_NAME)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

model.eval()

# Step 2: Define input prompt
prompt = "The capital of France is"

inputs = tokenizer(prompt, return_tensors="pt")

print("\nINPUT PROMPT:")
print(prompt)

# Step 3: Generate model outputs and inspect logits
with torch.no_grad():
    outputs = model(**inputs)

# Logits for the next token
logits = outputs.logits[0, -1, :]

print("\nLOGITS INFORMATION")
print("Logits shape:", tuple(logits.shape))

# Step 4: Convert logits into probabilities
probabilities = torch.softmax(logits, dim=-1)

# Step 5: Extract top 5 candidates
top_k = 5

top_probs, top_ids = torch.topk(probabilities, top_k)

print("\nTOP-K NEXT TOKEN CANDIDATES")
print("----------------------------------------")

for rank, (token_id, probability) in enumerate(
    zip(top_ids.tolist(), top_probs.tolist()), start=1
):
    token_text = tokenizer.decode([token_id])

    print(
        f"{rank}. Token: {repr(token_text):20s} "
        f"Token ID: {token_id:6d} "
        f"Probability: {probability:.6f} "
        f"({probability * 100:.2f}%)"
    )

# Step 6: Display the most probable next token
best_token_id = top_ids[0].item()
best_token = tokenizer.decode([best_token_id])

print("\nMOST PROBABLE NEXT TOKEN:")
print(repr(best_token))

print("\nNEXT-TOKEN ANALYSIS COMPLETED!")
