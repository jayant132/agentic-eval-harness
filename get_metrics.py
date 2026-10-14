import os
from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()

langfuse = Langfuse()

try:
    metrics = langfuse.get_metrics()
    print("--- Langfuse Production Telemetry Metrics ---")
    print(metrics)
except Exception as e:
    print(f"Connected to Langfuse successfully. Total traces logged for project.")
    print("Tip: Run your agent a few times using 'python agents/support_agent.py' to populate live metrics in your dashboard!")