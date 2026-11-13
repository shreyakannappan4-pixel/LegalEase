# LegalEase

An AI-assisted legal document generation platform powered by Google's Gemini API. LegalEase provides a simple interface for generating legal documents through user-provided information.

## Features

- AI-powered legal document generation using Gemini
- Streamlit-based user interface
- FastAPI backend for API handling
- Structured input fields for document generation
- Integration with Google's Gemini API

## Tech Stack

- **Language:** Python
- **AI:** Google Gemini API
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Server:** Uvicorn

## Project Structure

```text
LegalEase/
├── Image/
│   └── Logo.png
├── ai_core/
│   ├── __init__.py
│   ├── gemini_generator.py
│   └── vs code.py
├── frontend/
├── legalEaseAPI/
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python installed
- Google Gemini API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyakannappan4-pixel/LegalEase.git
   cd LegalEase/LegalEase
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your Gemini API key in a `.env` file as expected by the application.

### Running the Application

1. Start the FastAPI backend:

   ```bash
   uvicorn legalEaseAPI.main:app --reload
   ```

2. Open another terminal and start the Streamlit frontend:

   ```bash
   streamlit run frontend/app.py
   ```

3. Open the local URL displayed by Streamlit in your browser.

## Team Project

LegalEase was developed as a collaborative, AI-assisted team project. The project brought together frontend interaction, backend API handling, and Gemini-powered document generation.

## Disclaimer

LegalEase is an educational project and does not replace professional legal advice. Generated documents should be reviewed by a qualified legal professional before use.
