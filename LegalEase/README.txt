LEGALEASE - HOW TO RUN (Windows)

1. Open this LegalEase folder in VS Code (File > Open Folder).
2. Open .env and replace paste_your_key_here with your Gemini key
   (free at aistudio.google.com). Save with Ctrl+S.
3. Open a terminal (Ctrl + `) and run:
      python -m venv venv
      venv\Scripts\activate
      pip install -r requirements.txt
4. Start the backend (keep this terminal open):
      uvicorn legalEaseAPI.main:app --reload
5. Open a SECOND terminal (click + in the terminal panel), then:
      venv\Scripts\activate
      streamlit run frontend/app.py
6. Your browser opens http://localhost:8501. Fill the 4 boxes and click Generate.

Test case:
  Document Type: Freelance Work Contract
  Parties: Jane Doe (Service Provider), TechNova Inc. (Client)
  Terms: Work must be delivered by May 15, 2025; Payment within 7 days of invoice; Confidentiality must be maintained at all times
  Effective Date: April 15, 2025

To use your own logo, replace Image/Logo.png with your image (keep the name Logo.png).
