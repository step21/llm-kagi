import llm
import requests

@llm.hookimpl
def register_models(register):
    register(Markov())
    register(FastGPT())
    register(Summarizer())

class Markov(llm.Model):
    model_id = "markov"

    def execute(self, prompt, stream, response, conversation):
        return ["hello world"]

class FastGPT(llm.Model):
    model_id = "fastgpt"

    def execute(self, prompt, stream, response, conversation):
        return "hello this is fastgpt"

class Summarizer(llm.Model):
    model_id = "summarizer"
    base_url = 'https://kagi.com/api/v0/summarize'

    def execute(self, prompt, stream, response, conversation):
        return "hello this is the summarizer"
