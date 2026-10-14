# Agentic CI/CD Evaluation & Observability Harness (`agentic-eval-harness`)

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)
[![DeepEval](https://img.shields.io/badge/Evaluation-DeepEval-green.svg)](https://github.com/confident-ai/deepeval)
[![Langfuse](https://img.shields.io/badge/Observability-Langfuse-purple.svg)](https://langfuse.com/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama%20(Local)-informational.svg)](https://ollama.com/)
[![uv](https://img.shields.io/badge/Package%20Manager-uv-blueviolet.svg)](https://github.com/astral-sh/uv)

A production-grade, privacy-first **LLMOps framework** designed to treat agentic AI prompts, workflows, and tools like compiled code. This repository bridges the gap between prototype AI and production reliability by automating pre-merge regression testing and real-time runtime observability.

---

## 🏗️ System Architecture & Workflow

In enterprise AI engineering, updating an agent's system prompt or underlying tool graph without automated evaluation introduces silent regressions. This project implements a **dual-layer MLOps architecture**: offline CI/CD quality gates and online distributed tracing.

```mermaid
graph TD
    %% Styling
    classDef dev fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef cicd fill:#065f46,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef prod fill:#1e1b4b,stroke:#8b5cf6,stroke-width:2px,color:#fff;

    Developer([Developer Open PR]) -->|Triggers| CI[GitHub Actions CI/CD Runner]:::cicd
    
    sub_Evaluation["Pre-Merge Evaluation Pipeline (CI/CD)"]
    CI -->|1. Loads Ground Truth| Golden[Golden Dataset: test_data.json]:::dev
    CI -->|2. Executes Agent| Agent[LangGraph Support Agent: Llama 3.2:3b]:::dev
    CI -->|3. Grades Output| Judge[Custom DeepEval Judge via Ollama]:::dev
    
    Judge -->|Hallucination & Relevancy Checks| Gate{Pass Threshold >= 0.7?}:::cicd
    Gate -->|No: Blocks Merge| Fail([Block PR & Report Regression])::cicd
    Gate -->|Yes: Clears Quality Gate| Success([Allow Merge to Main])::cicd

    sub_Observability["Runtime Production Telemetry"]
    ProductionUser([End User Request]) --> ProdAgent[LangGraph Agent]:::prod
    ProdAgent -->|OpenTelemetry Callbacks| Langfuse[(Langfuse Cloud Dashboard)]:::prod
    Langfuse -->|Monitors Latency, Tokens & Traces| Analytics([Live Telemetry & Cost Tracking])::prod
🛠️ Production Tech Stack
Orchestration: LangGraph for managing stateful agent loops and context flow.

Local Execution & Judge: Ollama running llama3.2:3b for zero-cost, data-private inference.

Evaluation Framework: DeepEval utilizing custom model wrappers to run LLM-as-a-Judge metrics offline.

Testing Harness: Pytest parameterizing regression suites against structured golden datasets.

Runtime Observability: Langfuse capturing OpenTelemetry traces, token usage, and latencies.

Infrastructure Management: Astral uv for lightning-fast dependency resolution and virtual environments.

📂 Project Structure
Plaintext
agentic-eval-harness/
├── agents/
│   ├── __init__.py
│   └── support_agent.py      # LangGraph stateful IT agent + Langfuse tracing
├── tests/
│   ├── __init__.py
│   ├── test_data.json        # Golden dataset (Inputs, Contexts, Expected Outputs)
│   ├── custom_judge.py       # Custom DeepEval base LLM routing to Ollama JSON mode
│   └── test_agent.py         # Pytest test suite enforcing hallucination/relevancy thresholds
├── .github/
│   └── workflows/
│       └── eval.yml          # Automated GitHub Actions CI/CD pipeline
├── .env                      # Secure runtime keys (git-ignored)
├── pyproject.toml
├── requirements.txt
└── README.md
🚀 Quickstart & Local Installation
Prerequisites
Ensure Ollama is installed and running locally:

Bash
ollama pull llama3.2:3b
Create a free account on Langfuse to get your API keys.

Step-by-Step Setup
Clone the repository:

Bash
git clone [https://github.com/jayant132/agentic-eval-harness.git](https://github.com/jayant132/agentic-eval-harness.git)
cd agentic-eval-harness
Initialize environment using uv:

Bash
uv venv
source .venv/bin/activate
Install dependencies:

Bash
uv pip install langgraph langchain-ollama deepeval pytest python-dotenv langfuse langchain
uv pip freeze > requirements.txt
Configure Environment Secrets:
Create a .env file in the root directory:

Code snippet
LANGFUSE_PUBLIC_KEY=lf-pk-your_public_key_here
LANGFUSE_SECRET_KEY=lf-sk-your_secret_key_here
LANGFUSE_HOST=[https://cloud.langfuse.com](https://cloud.langfuse.com)
Run the Evaluation Test Harness:

Bash
deepeval test run tests/test_agent.py
📊 Sample Golden Dataset (test_data.json)
To prevent regressions, the framework evaluates the agent against structured factual truths representing real-world enterprise edge cases:

JSON
[
  {
    "input": "How do I request a new laptop?",
    "expected_output": "Submit a ticket through the IT service desk portal under 'Hardware Requests'. Manager approval is required.",
    "context": [
      "Employee hardware lifecycle: Laptops are refreshed every 3 years. For out-of-cycle replacements or new hires, submit a ticket via the IT service desk portal (Hardware Requests). All hardware requests require direct manager approval before fulfillment."
    ]
  }
]
💡 Key Engineering Takeaways for MNC Recruiter Evaluation
Decoupled MLOps Architecture: Separates offline evaluation (catching bugs before deployment via CI/CD test gates) from online observability (tracking user interactions and telemetry in production).

Zero Data Leakage: Fully local evaluation execution ensures sensitive corporate documents and source code never leave internal hardware during testing.

Strict Structured Output Handling: Overcomes the limitation of smaller local judge models by enforcing engine-level JSON formatting constraints to guarantee parsing reliability.

👨‍💻 Author
Built and maintained by an AI Engineer focused on building robust, observable, and reliable enterprise-grade autonomous systems.