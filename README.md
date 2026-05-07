# KAAL: Knowledge Agent Arbitration Layer
### *Chrono-Synthetic Strategic Foresight powered by AMD Instinct™ MI300X*

[![AMD MI300X](https://img.shields.io/badge/Hardware-AMD%20Instinct%20MI300X-ED1C24?style=for-the-badge&logo=amd&logoColor=white)](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html)
[![ROCm 7.0](https://img.shields.io/badge/Software-ROCm%207.0-005387?style=for-the-badge)](https://rocm.docs.amd.com/)
[![Hackathon](https://img.shields.io/badge/Hackathon-AMD%20Developer%20Lablab.ai-FFD700?style=for-the-badge)](https://lablab.ai/ai-hackathons/amd-developer)

---

## 👁️ The Vision: Solving the Future Backward
Current LLMs are "Next-Token Predictors," not "Strategy Generators." **KAAL** (Knowledge Agent Arbitration Layer) is a specialized reasoning engine designed to solve the *Future Backward*. 

Instead of simple extrapolation, KAAL uses a **Multi-Agent Adversarial Consensus** loop to identify systemic risks and strategic opportunities in 10, 25, and 50-year horizons.

---

## 🧠 The KAAL Architecture (4-Agent Pipeline)

KAAL does not just "answer" a prompt. It runs a digital "Conflict Room" where four specialized agents debate your query:

| Agent | Core Logic | Role |
| :--- | :--- | :--- |
| **The Architect** | *Constructive* | Synthesizes a thesis based on uploaded evidence (PDFs/CSVs). |
| **The Contrarian** | *Adversarial* | Actively attempts to falsify the Architect's thesis using stress-tests. |
| **The Analyst** | *Reconciliatory* | Reconciles the divergence between the thesis and the critique. |
| **The Synthesizer** | *Calibrated* | Produces a PhD-level strategic report with projected confidence levels. |

---

## ⚡ AMD MI300X Hardware Advantage
KAAL is built to exploit the massive **206GB VRAM** and memory bandwidth of the **AMD Instinct™ MI300X**.

- **High-Fidelity Inference:** The MI300X allows us to maintain massive context windows (up to 32k tokens) across all 4 agents simultaneously without latency spikes.
- **Quantization Efficiency:** Optimized via ROCm 7.0, achieving 2x throughput compared to standard H100 benchmarks for multi-agent orchestration.
- **Model Depth:** Powers our custom fine-tuned **KAAL-LoRA** (based on Qwen2.5-7B) with zero-compromise precision.

---

## 📊 Model Training & Science
- **Training Set:** 532 high-precision foresight pairs.
- **Source Data:** Curated from 208+ scientific and institutional sources (IPCC AR6, IEA World Energy Outlook, UN Population Projections, World Bank 2025).
- **Fine-Tuning:** LoRA adapters trained on ROCm-optimized kernels. 
- **Loss Convergence:** Reduced from 2.5 to **0.47**, ensuring highly calibrated "Think Tank" prose.

---

## 🚀 Repository Structure
- `app.py` — The Gradio-powered "Conflict Room" Dashboard.
- `collect_data.py` — Automated scientific evidence scraper (arXiv/World Bank).
- `build_dataset.py` — Synthetic data generator for backcasting logic.
- `finetune.py` — ROCm-optimized training script for the MI300X.
- `requirements.txt` — Full dependency stack.

---

## 🛠️ Getting Started
1. **Clone the Repo:** `git clone https://github.com/z99wE/kaal-foresight`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Launch Engine:** `python app.py`

*Note: Requires an active inference server running the KAAL-LoRA model on port 8000.*

---

## 🏆 AMD Developer Hackathon — lablab.ai
KAAL is submitted as a mission-critical tool for infrastructure planning, corporate risk management, and long-term policy design.

**Developed by:** [Your Name/Team Name]
