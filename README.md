# KAAL — Knowledge Agent Arbitration Layer
### *The Anti-Slop Intelligence Engine — Built on AMD MI300X*

> "Because the future is too important for AI-generated fluff."

**Live Demo:** https://attendee-unengaged-explain.ngrok-free.dev
**HuggingFace Space:** https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/kaal-foresight
**Model Weights:** https://huggingface.co/sf0Jmn/kaal-7b-lora

---

## Built for the AMD Developer Hackathon — lablab.ai

KAAL is a full-stack AI agent system built from scratch on **AMD Instinct MI300X** using **ROCm 7.0**. It connects every layer of the AI stack — from raw GPU compute and model fine-tuning to intelligent multi-agent workflows and a production-ready application.

---

## The Problem
Legacy AI tells you what happened. KAAL tells you what's coming. KAAL has a 50-year horizon. No AI slop.

## The Agent Architecture
Four adversarial agents (Architect, Contrarian, Analyst, Synthesizer) debate in real-time on AMD hardware to find the most resilient strategic truth.

## The Fine-Tuning Story
We fine-tuned a 7B model on the **AMD MI300X (206GB VRAM)** in under 3 hours with full precision. Training loss dropped 81% (2.5 → 0.47).

---

## Full AMD Stack
- **Hardware**: AMD Instinct MI300X VF (206GB VRAM)
- **Software**: ROCm 7.0, PyTorch 2.9.1+rocm6.4
- **Training**: Unsloth + HuggingFace PEFT
- **Context window**: 200,000 characters

---

## Repository Structure
- **app.py** — Gradio UI with 4-agent arbitration
- **collect_data.py** — Data collection APIs
- **build_dataset.py** — Training data generation
- **finetune.py** — LoRA fine-tuning code
- **requirements.txt** — Dependencies
