"""
Converts collected sources into KAAL training examples.
Uses Qwen-72B via HuggingFace transformers directly on AMD GPU. Free.
"""
import json, os, torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Loading Qwen-72B onto GPU...")
model_id = "Qwen/Qwen2.5-72B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)
print("Model loaded. GPU ready.")

KAAL_SYSTEM = """You are KAAL (Knowledge Across Aeons and Life-spans).
ALWAYS respond in exactly this format:

**10-year projection (confidence X%):** [specific finding with numbers]
**25-year projection (confidence Y%):** [specific finding with numbers]
**50-year projection (confidence Z%):** [specific finding with numbers]
**What this means today:** [specific, actionable insight]

Confidence MUST decrease with time. X > Y > Z. Always cite source type."""

with open("/root/data/sources.jsonl") as f:
    sources = [json.loads(l) for l in f if l.strip()]

out_path = "/root/data/kaal_train.jsonl"
examples = []

print(f"\nGenerating training data from {len(sources)} sources...\n")

for i, src in enumerate(sources):
    domain   = src.get("domain", "General")
    year     = src.get("year", 2024)
    priority = src.get("priority", "STANDARD")
    chunk    = src["content"][:800]
    n_pairs  = 3 if priority == "HIGH" else 2

    prompt = (
        f"This {domain} data is from {year}.\n"
        f"Generate {n_pairs} question-answer training pairs.\n\n"
        f"Return ONLY valid JSON array, no other text:\n"
        f'[{{"question": "...", "answer": "..."}}]\n\n'
        f"Source:\n{chunk}"
    )

    messages = [
        {"role": "system", "content": KAAL_SYSTEM},
        {"role": "user", "content": prompt}
    ]

    try:
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = tokenizer(text, return_tensors="pt").to("cuda")
        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=700,
                temperature=0.2,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )
        response = tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()
        response = response.replace("```json","").replace("```","").strip()
        pairs = json.loads(response)
        for p in pairs:
            if "question" in p and "answer" in p and len(p["answer"]) > 100:
                examples.append({
                    "messages": [
                        {"role": "system",    "content": KAAL_SYSTEM},
                        {"role": "user",      "content": p["question"]},
                        {"role": "assistant", "content": p["answer"]},
                    ],
                    "metadata": {"domain": domain, "year": year, "priority": priority}
                })
    except Exception as e:
        pass

    if (i + 1) % 25 == 0:
        print(f"  {i+1}/{len(sources)} sources → {len(examples)} examples")
        with open(out_path, "w") as f:
            for e in examples:
                f.write(json.dumps(e) + "\n")

with open(out_path, "w") as f:
    for e in examples:
        f.write(json.dumps(e) + "\n")

print(f"\n✅ Done: {len(examples)} examples → {out_path}")
