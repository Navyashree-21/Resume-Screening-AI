import json

from services.gemini_client import GeminiClient
from prompts.skill_prompt import SKILL_PROMPT


class SkillAgent:

    def __init__(self):
        self.llm = GeminiClient()

    def analyze(self, resume):

        prompt = SKILL_PROMPT.format(
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