import pytest
import json
from deepeval import assert_test
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from agents.support_agent import run_agent
from tests.custom_judge import LocalOllamaJudge

def load_goldens():
    with open("tests/test_data.json", "r") as f:
        return json.load(f)

local_mistral = LocalOllamaJudge(model_name="llama3.2:3b")

hallucination_metric = HallucinationMetric(threshold=0.5, model=local_mistral)
relevancy_metric = AnswerRelevancyMetric(threshold=0.7, model=local_mistral)
@pytest.mark.parametrize("golden", load_goldens())
def test_agent_responses(golden):
    actual_output = run_agent(
        query=golden["input"], 
        context=golden["context"][0] 
    )
    
    test_case = LLMTestCase(
        input=golden["input"],
        actual_output=actual_output,
        expected_output=golden["expected_output"],
        context=golden["context"],             
        retrieval_context=golden["context"]    
    )
    
    assert_test(test_case, [hallucination_metric, relevancy_metric])