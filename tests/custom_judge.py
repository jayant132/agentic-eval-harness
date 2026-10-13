from deepeval.models import DeepEvalBaseLLM
from langchain_ollama import ChatOllama

class LocalOllamaJudge(DeepEvalBaseLLM):
    def __init__(self, model_name="llama3.2:3b"):
        self.model = ChatOllama(model=model_name, temperature=0.0,format = "json")
        self.model_name = model_name

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        return chat_model.invoke(prompt).content

    async def a_generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        response = await chat_model.ainvoke(prompt)
        return response.content

    def get_model_name(self):
        return f"Local Ollama: {self.model_name}"