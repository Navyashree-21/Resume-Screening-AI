import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

    # 👇 This is the function you replace
    def generate(self, prompt):

        last_exception = None

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                last_exception = e

                print("\n==============================")
                print(f"Attempt {attempt + 1} failed")
                print("Error Type:", type(e).__name__)
                print("Error:", e)
                print("==============================\n")

                time.sleep(5)

        raise RuntimeError(
            f"Gemini API failed after 3 attempts.\n\nOriginal Error:\n{last_exception}"
        )