# KAAL — Knowledge Agent Arbitration Layer
### *The only Multi-Agent Reasoning engine built to solve the future backward.*
#### *The Anti-Slop Intelligence Engine — Built on AMD MI300X + ROCm*

> "Because the future is too important for AI-generated fluff."

| | Link |
|---|---|
| 🚀 **Live Demo** | [Launch KAAL](https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/kaal-foresight) |
| 🤗 **HuggingFace Space** | [kaal-foresight](https://huggingface.co/spaces/lablab-ai-amd-developer-hackathon/kaal-foresight) |
| 🧠 **Model Weights (LoRA)** | [kaal-7b-lora](https://huggingface.co/sf0Jmn/kaal-7b-lora) |
| 📦 **GGUF Model** | [kaal-7b-gguf](https://huggingface.co/sf0Jmn/kaal-7b-gguf) |
| 💻 **GitHub** | [kaal-foresight](https://github.com/z99wE/kaal-foresight) |

---

## Built for the AMD Developer Hackathon — lablab.ai

KAAL is a full-stack AI agent system built from scratch on **AMD Instinct MI300X** using **ROCm 7.0**. It connects every layer of the AMD AI stack — from raw GPU compute and model fine-tuning to intelligent multi-agent workflows and a live production application — exactly what this hackathon is designed for.

---

## The Problem

Legacy AI tells you what happened. KAAL tells you what's coming — and why it's inevitable.

The world's most consequential decisions — infrastructure planning, workforce strategy, capital allocation — are being made with tools that have a 2-year knowledge horizon. KAAL has a 50-year one. And unlike generic LLMs, it gives you crisp, calibrated answers. Not AI slop.

---

## Application of Technology — Full AMD Stack

| Layer | Technology |
|-------|-----------|
| Hardware | AMD Instinct MI300X VF — 206GB HBM3 VRAM |
| GPU Stack | ROCm 7.0 — open-source, no proprietary lock-in |
| Framework | PyTorch 2.9.1+rocm6.4 |
| Training | Unsloth + HuggingFace PEFT + TRL on AMD |
| Base Model | Qwen2.5-7B-Instruct — LoRA fine-tuned on AMD MI300X |
| Data Engine | Qwen2.5-72B on AMD MI300X — synthetic training data generation |
| Quantization | GGUF Q4_K_M via llama.cpp on AMD — 15GB → 4.4GB |
| Serving | GGUF inference via llama-cpp-python — runs free on CPU permanently |
| UI | Gradio — live on HuggingFace Spaces |

The entire pipeline — data collection, synthetic data generation, fine-tuning, quantization — ran on a single AMD MI300X. No NVIDIA. No proprietary stack. Pure ROCm.

---

## The Agent Architecture

Four autonomous adversarial agents debate every query. No fluff. No hallucinations. Just arbitrated intelligence.

| Agent | Role |
|-------|------|
| **Architect** | Builds strategic thesis from evidence and uploaded documents |
| **Contrarian** | Attacks and stress-tests every assumption |
| **Analyst** | Reconciles the conflict into balanced findings |
| **Synthesizer** | Delivers a PhD-level calibrated forecast — concise, complete, never repeats |

Input: Any PDF, CSV, Excel, image, or strategic question.
Output: Crisp 10, 25, 50-year projections with confidence levels. Always ends at a complete sentence. Never slop.

---

## The Fine-Tuning Story — Why AMD Made This Possible

Most teams prompt-engineer their way to mediocrity. We fine-tuned.

Fine-tuning a **7-billion parameter model** is not trivial. It requires holding the entire model in GPU memory during forward and backward passes, managing gradient checkpointing across hundreds of steps, and keeping training stable without loss spikes or mode collapse. On a standard setup this takes days and costs thousands.

On the **AMD MI300X with 206GB HBM3 VRAM**, we ran the full fine-tune in under 3 hours — no quantization, no model sharding, full bfloat16 precision. The MI300X held the entire 7B model plus optimizer states, gradients, and activations simultaneously. ROCm 7.0 handled the entire training stack natively.

Then we used **llama.cpp on the same AMD server** to quantize the merged model to GGUF Q4_K_M format — compressing 15GB → 4.4GB with minimal quality loss. The result runs permanently free on HuggingFace CPU Spaces.

- Training loss: **2.5 → 0.47** (81% reduction)
- Training examples: **532** from **208** scientific sources
- Sources: IPCC, IEA, WHO, WEF, World Bank (2024-2026)
- Fine-tune time: **under 3 hours** on AMD MI300X
- GGUF size: **4.4GB** (Q4_K_M quantization)

KAAL's forecasting behavior is baked into the weights — not bolted on with a system prompt. Fine-tuned, not prompted.

---

## Business Value & Real-World Impact

- **TAM:** $4.5B strategic foresight consulting market (2025)
- **Buyers:** Infrastructure firms, sovereign wealth funds, HR strategy teams, defense contractors
- **Replaces:** $50,000/month analyst retainer panels with one fine-tuned agentic system
- **Cost on AMD:** $1.99/hr for training — then free forever via GGUF on CPU
- Zero cloud dependency. Zero per-query API cost. Full IP ownership.

| Sector | Business Goal | Legacy AI | KAAL Foresight |
|--------|--------------|-----------|----------------|
| Infrastructure | 30-Year Planning | Ignores climate shifts | Maps 50-year risks |
| Corporate HR | Workforce Agility | Fails to predict skill gaps | Forecasts 2050 labor shifts |
| Finance & Risk | Portfolio Stability | Uses past loss trends | Runs adversarial stress-tests |
| Energy | Grid Transition | Extrapolates today's tech | Synthesizes global trends |

---

## Originality

- **First foresight engine** built with adversarial multi-agent arbitration — agents debate, not just summarize
- **End-to-end AMD pipeline:** data collection → 72B synthetic data generation → 7B fine-tuning → GGUF quantization — all on one MI300X
- **Smart PDF compression:** 500-page documents → top 10 query-relevant chunks via keyword scoring — no vector DB needed
- **Anti-repetition architecture:** hard sentence-boundary trimming + deduplication at every agent layer
- **Free permanent deployment:** GGUF Q4 runs on HuggingFace CPU Spaces — no GPU needed after training

---

## Repository Structure

| File | Purpose |
|------|---------|
| `app.py` | Gradio UI — 4-agent arbitration pipeline, GGUF inference |
| `collect_data.py` | Data collection: arXiv, World Bank, WHO APIs |
| `build_dataset.py` | Synthetic training data via Qwen-72B on AMD |
| `finetune.py` | LoRA fine-tuning on AMD MI300X + ROCm 7.0 |
| `requirements.txt` | Python dependencies |

---

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

The app loads the GGUF model directly from HuggingFace. Set `HF_TOKEN` environment variable for private model access.

---

*AMD Developer Hackathon — lablab.ai*
*Stack: AMD MI300X · ROCm 7.0 · Qwen2.5 · GGUF · llama-cpp-python · HuggingFace · Gradio*
*Judging: Application of Technology · Business Value · Originality · Presentation*
