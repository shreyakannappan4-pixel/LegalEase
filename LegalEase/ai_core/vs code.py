import os
import time

import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

# Read the GEMINI_API_KEY from the .env file
load_dotenv()


class GeminiDocumentGenerator:
    """The 'chef': takes the user's details and asks Gemini to write the legal document."""

    def __init__(self, model_name: str = "gemini-3.5-flash-lite"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Add it to your .env file like this:\n"
                "GEMINI_API_KEY=your_key_here"
            )
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_document(self, document_type, parties, terms, dates):
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'.\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions (separated by semicolons): {terms}\n"
            "Ensure formal legal structure with multiple numbered sections and legal clauses. "
            "Include a signature block at the end."
        )

        # If the free-plan limit (429) is hit, wait and try again (up to 3 times)
        for attempt in range(3):
            try:
                response = self.model.generate_content(
                    prompt, request_options={"retry": None, "timeout": 120}
                )
                return response.text
            except ResourceExhausted:
                if attempt == 2:
                    raise
                time.sleep(65)


# Quick test: run  python ai_core/gemini_generator.py
if __name__ == "__main__":
    generator = GeminiDocumentGenerator()
    print(
        generator.generate_document(
            "Freelance Work Contract",
            "Jane Doe (Service Provider), TechNova Inc. (Client)",
            "Work must be delivered by May 15, 2025; Payment within 7 days of invoice",
            "April 15, 2025",
        )
    )