# Agentic CI/CD Evaluation Pipeline (`agentic-eval-harness`)

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)
[![DeepEval](https://img.shields.io/badge/Testing-DeepEval-green.svg)](https://github.com/confident-ai/deepeval)
[![Ollama](https://img.shields.io/badge/LLM-Ollama%20(Local)-purple.svg)](https://ollama.com/)
[![uv](https://img.shields.io/badge/Package%20Manager-uv-blueviolet.svg)](https://github.com/astral-sh/uv)

A production-grade, zero-cost LLMOps evaluation framework designed to treat agentic prompts and workflows like compiled code. This pipeline runs automated regression testing against a **Golden Dataset** using local LLM-as-a-Judge architecture, preventing hallucinations and breaking changes from merging into production.

---

## 🏗️ Architecture & System Design

In enterprise AI engineering, updating an agent's system prompt or underlying tool graph without automated evaluation introduces silent regressions. This repository solves that problem by embedding quality gates directly into the development lifecycle.

```text
[ Developer PR ] 
       │
       ▼
[ GitHub Actions CI/CD Runner ]
       │
       ├─► 1. LangGraph Support Agent (Executes Query + Context using Llama 3.2:3b)
       │
       ├─► 2. Golden Dataset (Loaded from test_data.json)
       │
       └─► 3. Custom DeepEval Judge (Grades actual output vs. expected output via Ollama)
              │
              ├─► Hallucination Metric (Threshold: 0.3)
              └─► Answer Relevancy Metric (Threshold: 0.5)
                     │
                     ▼
          [ Pass / Block Merge Decision ]

```

---

## 🚀 Tech Stack

* **Orchestration:** LangGraph (Stateful, production-grade agent workflows).
* **Local Execution:** Ollama running `llama3.2:3b` for zero cloud dependency and data privacy.
* **Evaluation Framework:** DeepEval (Custom base class wrapper routing evaluation prompts locally).
* **Testing Harness:** Pytest parameterizing multi-turn and single-turn golden datasets.
* **Package Management:** `uv` by Astral for lightning-fast environment provisioning.

---

## 📂 Project Structure

```text
agentic-eval-harness/
├── agents/
│   ├── __init__.py
│   └── support_agent.py      # LangGraph stateful IT support agent
├── tests/
│   ├── __init__.py
│   ├── test_data.json        # Golden dataset (Ground truths & contexts)
│   ├── custom_judge.py       # Custom DeepEval runner hooked to local Ollama
│   └── test_agent.py         # Pytest test harness orchestrating metrics
├── .github/
│   └── workflows/
│       └── eval.yml          # Automated CI/CD workflow pipeline
├── pyproject.toml
├── requirements.txt
└── README.md

```

---

## 🛠️ Getting Started Locally

### Prerequisites

* Ensure [Ollama](https://ollama.com/) is installed and running locally with the model pulled:
```bash
ollama pull llama3.2:3b

```



### Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/agentic-eval-harness.git](https://github.com/YOUR_USERNAME/agentic-eval-harness.git)
cd agentic-eval-harness

```


2. **Initialize environment with `uv`:**
```bash
uv venv
source .venv/bin/activate

```


3. **Install dependencies:**
```bash
uv pip install langgraph langchain-ollama deepeval pytest

```


4. **Run the Evaluation Harness:**
```bash
deepeval test run tests/test_agent.py

```



---

## 📊 Sample Test Case Structure (`test_data.json`)

The evaluation suite relies on a structured JSON ground-truth dataset representing enterprise IT support scenarios:

```json
[
  {
    "input": "How do I request a new laptop?",
    "expected_output": "Submit a ticket through the IT service desk portal under 'Hardware Requests'. Manager approval is required.",
    "context": [
      "Employee hardware lifecycle: Laptops are refreshed every 3 years. For out-of-cycle replacements or new hires, submit a ticket via the IT service desk portal (Hardware Requests). All hardware requests require direct manager approval before fulfillment."
    ]
  }
]

```

---

## 💡 Engineering Takeaway for Recruiters

* **Zero Data Leakage:** Fully containerized/local evaluation ensures sensitive enterprise documentation never leaves local memory during test runs.
* **Deterministic Guardrails:** Bypasses loose conversational evaluation by enforcing strict API-level formatting and mathematical metric thresholds.
* **CI/CD Integration Ready:** Easily translatable to cloud runners to block broken prompt deployments automatically.

---

## 👨‍💻 Author

Built with precision by an AI Engineer passionate about reliable, observable, and production-ready agentic systems.

```

---

<FollowUp label="Ready to add the GitHub Actions workflow file?" query="The README is set. Now give me the code for `.github/workflows/eval.yml` so we can complete the automation setup."/>

```
