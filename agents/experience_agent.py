import json

from services.gemini_client import GeminiClient
from prompts.experience_prompt import EXPERIENCE_PROMPT


class ExperienceAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def analyze(self, resume):

        prompt = EXPERIENCE_PROMPT.format(
            resume=resume
        )

        response = self.llm.generate(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "").strip()

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            raise ValueError(
                "Gemini returned invalid JSON."
            )