import os, json, torch
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset

os.environ["HSA_OVERRIDE_GFX_VERSION"] = "9.4.2"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Qwen/Qwen2.5-7B-Instruct",
    max_seq_length=2048,
    load_in_4bit=False,
    dtype=torch.bfloat16,
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    lora_alpha=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    use_gradient_checkpointing="unsloth",
    random_state=42,
)

dataset = load_dataset("json", data_files="/root/data/kaal_train.jsonl", split="train")

# FIXED: Handles both single test examples and full training batches
def format_examples(examples):
    messages = examples["messages"]
    # If messages[0] is a dict, it's a single example (test phase)
    if isinstance(messages[0], dict):
        return [tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)]
    # If messages[0] is a list, it's a batch (training phase)
    return [tokenizer.apply_chat_template(msg, tokenize=False, add_generation_prompt=False) for msg in messages]

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    formatting_func=format_examples,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
    args=SFTConfig(
        output_dir="/root/kaal-lora",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        weight_decay=0.01,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        bf16=True,
        fp16=False,
        logging_steps=5,
        optim="adamw_torch",
        gradient_checkpointing=True,
        dataloader_pin_memory=False,
        dataloader_num_workers=0,
        report_to="none",
        save_strategy="epoch",
        seed=42,
    ),
)

print("Starting training...")
trainer.train()

model.save_pretrained("/root/kaal-lora")
tokenizer.save_pretrained("/root/kaal-lora")
print("\n✅ KAAL fine-tune complete! Saved to /root/kaal-lora")
