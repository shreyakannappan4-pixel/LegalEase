# LegalEase
### AI-Assisted Legal Document Generation Platform

LegalEase is an AI-assisted legal document generation application that explores the use of generative artificial intelligence to simplify the preparation of structured legal documents.

The application integrates Google's Gemini API with a Python-based backend and an interactive Streamlit frontend. Users can provide document details, generate legal text, preview the output, make edits and download the generated document in multiple formats.

The project demonstrates the integration of generative AI, REST API communication, document formatting and downloadable file generation in a single application.

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Project Objectives](#project-objectives)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Application Architecture](#application-architecture)
- [Project Structure](#project-structure)
- [Application Workflow](#application-workflow)
- [AI Integration](#ai-integration)
- [Document Formatting and Export](#document-formatting-and-export)
- [Installation and Setup](#installation-and-setup)
- [Environment Configuration](#environment-configuration)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Error Handling](#error-handling)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Development Note](#development-note)
- [Disclaimer](#disclaimer)

---

## Overview

Legal document preparation involves organizing information into a structured format using formal language and appropriate sections.

LegalEase explores how generative AI can assist with this process through an interactive document generation workflow.

The application accepts four primary inputs:

- Document type
- Parties involved
- Terms and conditions
- Effective date

These details are passed to Google's Gemini API through a FastAPI backend. The generated content is returned to the Streamlit interface, where users can preview and edit the document before downloading it.

LegalEase also supports exporting generated content into TXT, DOCX and PDF formats.

## Problem Statement

Preparing formal documents can be challenging for individuals who are unfamiliar with legal terminology, document structures and formatting conventions.

LegalEase explores a simplified approach by combining a guided input interface with generative AI.

The application aims to:

- Simplify the initial document preparation process.
- Convert user-provided information into structured document content.
- Provide an interactive document preview.
- Allow users to edit generated content.
- Support multiple downloadable document formats.

## Project Objectives

1. Explore practical applications of generative AI in document preparation.
2. Integrate Google's Gemini API into a Python application.
3. Develop a user interface using Streamlit.
4. Implement backend request handling using FastAPI.
5. Generate structured text using user-provided information.
6. Support document formatting and export in multiple file formats.
7. Demonstrate communication between frontend, backend and AI components.

---

## Features

### 1. AI-Powered Legal Document Generation

LegalEase integrates Google's Gemini API to generate document content based on information provided by the user.

The generation process uses four inputs:

| Input | Description |
|---|---|
| Document Type | Specifies the requested document, such as an agreement, contract or NDA |
| Parties Involved | Identifies the individuals or organizations involved |
| Terms and Conditions | Contains the conditions supplied by the user |
| Effective Date | Specifies the document's effective date |

The application combines these inputs into a structured prompt requesting formal sections, legal clauses and a signature block.

### 2. Interactive Streamlit Interface

The frontend provides a simple interface for entering document details.

Features include:
- Text input for document type.
- Text areas for parties and terms.
- Effective date input.
- Document generation button.
- Input validation before submission.
- Loading indicator while the document is generated.

### 3. FastAPI Backend

The backend exposes a document generation endpoint that receives structured requests from the frontend.

It uses a Pydantic request model to define the expected input fields and connects the request to the Gemini document generation component.

### 4. Document Preview

After successful generation, the application displays the returned content in a formatted HTML preview.

The preview distinguishes headings, bullet points and regular paragraphs to improve readability.

### 5. Document Editing

Users can open an editing area and modify the generated text before downloading it.

The application maintains the generated content using Streamlit session state during the active session.

### 6. Multiple Download Formats

Generated documents can be downloaded in three formats:

| Format | Implementation | Description |
|---|---|---|
| TXT | Plain text | Downloads the generated document as text |
| DOCX | python-docx | Creates a formatted Word document |
| PDF | FPDF | Creates a downloadable PDF document |

### 7. Document Formatting

The document formatting component includes:
- Heading identification.
- Bullet-point formatting.
- Text sanitization.
- Logo placement when the logo file is available.
- Document title formatting.
- Footer text.
- A summary-of-terms table in DOCX exports.

### 8. API Error Handling

The application includes handling for common request failures, including:
- Missing or invalid Gemini API configuration.
- Gemini API errors.
- API quota exhaustion.
- Backend connection failures.
- Request timeouts.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Backend | FastAPI |
| API Server | Uvicorn |
| AI Integration | Google Gemini API |
| API Communication | Requests |
| Data Validation | Pydantic |
| DOCX Generation | python-docx |
| PDF Generation | FPDF |
| Environment Configuration | python-dotenv |
| Image Processing | Pillow |
| HTML Formatting | Python HTML utilities |

---

## Application Architecture

LegalEase follows a frontend-backend architecture with a separate AI integration component.

### Architecture Components

**1. Frontend Layer: Streamlit**

The Streamlit application collects user input, validates required fields, communicates with the backend and displays the generated document.

**2. Backend Layer: FastAPI**

The FastAPI application exposes the `/generate` endpoint, validates incoming request data through Pydantic and invokes the document generation component.

**3. AI Integration Layer: Gemini**

The `GeminiDocumentGenerator` class manages API configuration, prompt construction and communication with Google's Gemini model.

**4. Document Formatting Layer**

The formatting module handles HTML previews, text sanitization and document generation in TXT, DOCX and PDF formats.

### Architecture Diagram

```text
                 USER
                   |
                   v
          STREAMLIT FRONTEND
                   |
          User Input Validation
                   |
                   v
          HTTP POST REQUEST
                   |
                   v
             FASTAPI
             /generate
                   |
          PYDANTIC REQUEST MODEL
                   |
                   v
         GEMINI DOCUMENT GENERATOR
                   |
             PROMPT CREATION
                   |
                   v
              GEMINI API
                   |
                   v
          GENERATED DOCUMENT
                   |
                   v
          STREAMLIT FRONTEND
                   |
          +--------+--------+
          |        |        |
          v        v        v
        PREVIEW   EDIT    DOWNLOAD
                            |
                    +-------+-------+
                    |       |       |
                    v       v       v
                   TXT     DOCX     PDF
```

---

## Project Structure

```text
LegalEase/                         # GitHub repository root
│
├── .gitignore
├── README.md
│
└── LegalEase/                     # Application directory
    │
    ├── Image/
    │   └── Logo.png
    │
    ├── ai_core/
    │   ├── __init__.py
    │   ├── gemini_generator.py
    │   └── vs code.py
    │
    ├── frontend/
    │   ├── app.py
    │   └── formatters.py
    │
    ├── legalEaseAPI/
    │   ├── main.py
    │   └── routes.py
    │
    ├── requirements.txt
    └── README.txt
```

The application is organized into separate components for AI integration, frontend interaction, backend API handling and document formatting.

---

## Application Workflow

The application follows the workflow below:

**Step 1: User Input**

The user provides the document type, involved parties, terms and effective date through the Streamlit interface.

**Step 2: Input Validation**

The frontend checks that all four required fields contain information before submitting the request.

**Step 3: API Communication**

The frontend sends a POST request to the FastAPI `/generate` endpoint using the Requests library.

**Step 4: Request Processing**

FastAPI validates the incoming data through the `DocumentRequest` Pydantic model.

**Step 5: AI Document Generation**

The backend invokes `GeminiDocumentGenerator`, which constructs a prompt and submits it to the Gemini API.

**Step 6: Generated Output**

The generated document text is returned by the backend as a JSON response.

**Step 7: Preview and Editing**

The frontend sanitizes and displays the generated content. Users can optionally edit the text.

**Step 8: Document Export**

The final content can be downloaded in TXT, DOCX or PDF format.

---

## AI Integration

The AI integration is implemented in:

`ai_core/gemini_generator.py`

The application uses Google's Generative AI Python SDK to communicate with the Gemini API.

### GeminiDocumentGenerator

The `GeminiDocumentGenerator` class manages the document generation process.

Its responsibilities include:

- Loading the Gemini API key from the environment.
- Configuring the Gemini API client.
- Initializing the selected Gemini model.
- Constructing prompts using user-provided information.
- Generating document content.
- Handling API quota exhaustion through retry attempts.

### Prompt Construction

The application combines the following information into a structured prompt:

- Requested document title.
- Involved parties.
- Effective date.
- Terms and conditions.

The prompt requests formal document formatting, numbered sections, legal clauses and a signature block.

### API Rate-Limit Handling

The implementation handles the `ResourceExhausted` exception.

When a quota-exhaustion error occurs, the application waits for 65 seconds before retrying the generation request. It allows up to three attempts before raising the exception.

---

## Document Formatting and Export

Document formatting is implemented in:

`frontend/formatters.py`

The module contains functions for processing generated text and preparing downloadable documents.

### Text Sanitization

The `sanitize_text()` function normalizes selected typographic characters, removes Markdown formatting markers and cleans generated text before presentation.

### HTML Preview

The `format_html_preview()` function converts generated text into an HTML-based preview.

It identifies:
- Numbered headings.
- Short heading lines.
- Bullet points.
- Regular paragraphs.

HTML escaping is applied to text before inserting it into the preview.

### DOCX Generation

The `format_docx()` function uses the `python-docx` library.

The generated Word document includes:
- Times New Roman font.
- A formatted document title.
- The application logo when available.
- Heading and bullet formatting.
- A summary-of-terms table.
- Footer text.

### PDF Generation

The `format_pdf()` function uses FPDF to create a PDF document.

The generated PDF includes:
- A document title.
- Logo placement when available.
- Heading formatting.
- Bullet-point formatting.
- Paragraph content.
- Footer text.

### TXT Export

The generated text can also be downloaded directly as a `.txt` file.

---

## Installation and Setup

### Prerequisites

Before running the application, ensure that you have:

- Python installed.
- pip package manager.
- Git.
- A valid Google Gemini API key.
- An active internet connection for Gemini API requests.

### Step 1: Clone the Repository

```bash
git clone https://github.com/shreyakannappan4-pixel/LegalEase.git
```

Navigate to the application directory:

```bash
cd LegalEase/LegalEase
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

LegalEase uses environment variables to configure Gemini API access.

Create a `.env` file in the application directory.

Add the following:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual API key.

The application loads this variable using `python-dotenv`.

**Security Note:** Never upload your `.env` file or expose API credentials in a public repository.

---

## Running the Application

LegalEase requires the FastAPI backend and Streamlit frontend to run in separate terminals.

### Terminal 1: Start the Backend

From the application directory:

```bash
uvicorn legalEaseAPI.main:app --reload
```

The FastAPI backend will be available locally at:

`http://127.0.0.1:8000`

The API root endpoint can be accessed at:

`http://127.0.0.1:8000/`

### Terminal 2: Start the Frontend

Open a second terminal in the same application directory.

Activate the virtual environment if necessary, then execute:

```bash
streamlit run frontend/app.py
```

Open the local URL displayed in the terminal to access the application.

### Using LegalEase

1. Enter the required document type.
2. Provide the parties involved.
3. Enter the terms and conditions, separating individual terms with semicolons.
4. Enter the effective date.
5. Click **Generate Document**.
6. Review the generated document.
7. Use the editing option if modifications are required.
8. Download the document in TXT, DOCX or PDF format.

---

## API Reference

### Generate Legal Document

**Endpoint:** `POST /generate`

**Description:** Accepts document information and returns AI-generated document content.

### Request Body

```json
{
  "document_type": "Freelance Work Contract",
  "parties": "Jane Doe (Service Provider), TechNova Inc. (Client)",
  "terms": "Work must be delivered by May 15, 2025; Payment within 7 days of invoice",
  "dates": "April 15, 2025"
}
```

### Response

```json
{
  "document": "Generated legal document content..."
}
```

The response contains the generated document as a text string.

---

## Error Handling

The application includes error handling across its frontend, backend and AI integration components.

| Error | Handling |
|---|---|
| Missing input fields | Displays a validation warning in Streamlit |
| Missing Gemini API key | Returns a backend HTTP 500 error |
| Gemini API failure | Returns a backend HTTP 502 error |
| Gemini quota exhaustion | Waits and retries generation |
| Backend connection failure | Displays a connection error |
| Request timeout | Displays a timeout message |

---

## Limitations

- Generated documents may contain inaccurate or incomplete information.
- Output quality depends on the user-provided information and AI model response.
- The application does not independently verify legal correctness.
- Gemini API access requires a valid API key and internet connection.
- API quota restrictions may affect document generation.
- PDF generation uses built-in Latin-compatible fonts, so some special characters may not render correctly.
- Generated documents require human review before practical use.

---

## Future Improvements

Potential areas for further development include:

- Additional legal document templates.
- Improved input validation and error reporting.
- More comprehensive document formatting.
- Enhanced PDF typography and Unicode support.
- Document history and retrieval.
- Improved API security and request validation.
- Automated testing of frontend, backend and AI integration.
- Expanded document export options.

---

## Development Note

LegalEase is an AI-assisted software project. AI-generated code assistance was used during implementation. The project demonstrates the integration of generative AI, API-based backend communication, interactive frontend functionality and document generation.

---

## Disclaimer

LegalEase is an educational prototype intended to demonstrate generative AI applications in document preparation.

It does not provide professional legal advice, establish an attorney-client relationship or guarantee the legal validity of generated documents.

All generated documents should be reviewed by a qualified legal professional before being used for actual legal purposes.

---

## Repository

**GitHub:** https://github.com/shreyakannappan4-pixel/LegalEase
