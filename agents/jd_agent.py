import json

from services.gemini_client import GeminiClient
from prompts.jd_prompt import JD_PROMPT


class JDAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def analyze(self, resume, jd):

        prompt = JD_PROMPT.format(
            resume=resume,
            jd=jd
        )

        response = self.llm.generate(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "").strip()

        return json.loads(response)