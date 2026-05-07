# KAAL — Knowledge Agent Arbitration Layer
### *The Anti-Slop Intelligence Engine — Built on AMD MI300X + ROCm*

> "Because the future is too important for AI-generated fluff."

**Live Demo:** https://attendee-unengaged-explain.ngrok-free.dev
**HuggingFace Space:** https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/kaal-foresight
**Model Weights:** https://huggingface.co/sf0Jmn/kaal-7b-lora

---

## What is KAAL?

KAAL is a full-stack AI agent system that connects every layer of the AMD AI stack — from raw GPU compute and model fine-tuning to autonomous multi-agent workflows and a live production application.

Most AI gives you confident-sounding guesses. KAAL gives you **arbitrated intelligence** — four autonomous agents that debate, attack, reconcile, and deliver calibrated long-horizon forecasts. Crisp. Complete. No repetition. No slop.

---

## The Problem It Solves

The world's most consequential decisions — infrastructure planning, workforce strategy, capital allocation — are being made with tools that have a 2-year knowledge horizon. KAAL has a 50-year one.

Legacy AI tells you what happened. KAAL tells you what's coming — and why it's inevitable.

---

## Agent Architecture — AI Agents on AMD

Four autonomous adversarial agents run entirely on AMD MI300X:

| Agent | Role |
|-------|------|
| **Architect** | Constructs strategic thesis from evidence and uploaded documents |
| **Contrarian** | Attacks and stress-tests every assumption |
| **Analyst** | Reconciles conflict into calibrated findings |
| **Synthesizer** | Delivers PhD-level forecast — concise, complete, never repeats |

Upload any PDF, CSV, Excel, or document. Ask any strategic question. Get 10, 25, and 50-year projections with confidence levels — in seconds.

---

## AMD Technology Stack

| Layer | Technology |
|-------|-----------|
| Hardware | AMD Instinct MI300X VF — 206GB HBM3 VRAM |
| GPU Stack | ROCm 7.0 — open-source, no proprietary lock-in |
| Framework | PyTorch 2.9.1+rocm6.4 |
| Training | Unsloth + HuggingFace PEFT + TRL on AMD |
| Base Model | Qwen2.5-7B-Instruct — LoRA fine-tuned on AMD |
| Data Engine | Qwen2.5-72B running on AMD MI300X for synthetic data generation |
| Serving | Custom HuggingFace Transformers inference server |
| UI | Gradio — live on AMD GPU server |

---

## The Fine-Tuning Story

Fine-tuning a 7-billion parameter model is not trivial. It requires holding the entire model in GPU memory during forward and backward passes, managing gradient checkpointing, and keeping training stable across hundreds of steps without loss spikes.

On a standard setup this takes days. On **AMD MI300X with 206GB HBM3**, we ran the full fine-tune in under 3 hours — full bfloat16 precision, no quantization, no model sharding. ROCm 7.0 handled the entire training stack natively.

- Training loss: **2.5 → 0.47** (81% reduction)
- Training examples: **532** generated from **208** scientific sources
- Sources: IPCC, IEA, WHO, WEF, World Bank (2024-2026)
- Context window: **200,000 characters** per query
- Fine-tune time: **under 3 hours** on AMD MI300X

KAAL's forecasting behavior is baked into the weights — not bolted on with a system prompt. Fine-tuned, not prompted.

---

## Business Value & Real-World Impact

- **TAM:** $4.5B strategic foresight consulting market (2025)
- **Buyers:** Infrastructure firms, sovereign wealth funds, HR strategy teams, defense contractors
- **Replaces:** $50,000/month analyst retainer panels with one fine-tuned agentic system
- **Cost on AMD:** $1.99/hr — the MI300X makes enterprise-grade AI economically viable

Zero cloud dependency. Zero per-query API cost. Full IP ownership.

---

## Originality

- First foresight engine built with adversarial multi-agent arbitration
- Training data pipeline: 72B model generates synthetic examples on the same AMD hardware that runs inference
- Smart PDF compression: 500-page documents → top 10 query-relevant chunks via keyword scoring
- Anti-repetition architecture: hard sentence-boundary trimming + deduplication at every agent layer

---

## Repository Structure app.py              — Gradio UI — 4-agent arbitration pipeline
collect_data.py     — Data collection: arXiv, World Bank, WHO APIs
build_dataset.py    — Synthetic training data via Qwen-72B on AMD
finetune.py         — LoRA fine-tuning on AMD MI300X + ROCm 7.0
requirements.txt    — Python dependencies    ---

## How to Run

```bash
pip install -r requirements.txt
# Set AMD_IP environment variable to your inference server
export AMD_IP=your-server-ip
python app.py
```

---

*AMD Developer Hackathon — lablab.ai*
*Stack: AMD MI300X · ROCm 7.0 · Qwen2.5 · HuggingFace · Gradio*
*Theme: AI Agents · Full-Stack AMD · Real-World Impact*
