# LegalEase
### AI-Assisted Legal Document Generation Platform

LegalEase is an AI-assisted legal document generation application designed to simplify the process of creating structured legal documents through generative artificial intelligence.

Built using Python, FastAPI, Streamlit and Google's Gemini API, the application combines an interactive frontend with a backend API and an AI-powered document generation component.

The project explores how generative AI can make document preparation more accessible through a guided user interface and automated text generation.

---

## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Project Objectives](#project-objectives)
- [Key Features](#key-features)
- [Application Architecture](#application-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Application Workflow](#application-workflow)
- [Installation and Setup](#installation-and-setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Use Cases](#use-cases)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Development Note](#development-note)
- [Disclaimer](#disclaimer)

---

## Overview

Understanding and preparing legal documents can be challenging for individuals who are unfamiliar with legal terminology and document structures.

LegalEase explores the application of generative AI to simplify this process.

The application accepts user-provided information through a structured interface and uses Google's Gemini API to generate document content. A Streamlit frontend provides the user interaction layer, while a FastAPI backend handles API requests and connects the application components.

The project demonstrates an AI-assisted approach to document generation by combining a user interface, backend communication and a generative AI service.

## Problem Statement

Preparing structured legal documents often requires familiarity with formal language, formatting conventions and relevant information.

For users without this familiarity, getting started with document preparation can be difficult.

LegalEase explores a technology-based approach to this challenge by providing:

- A simplified interface for entering document-related information.
- AI-assisted generation of structured document content.
- A backend service to manage application requests.
- Integration with a generative AI model for text generation.

The objective is to demonstrate how AI-powered applications can support document preparation while keeping human review essential.

## Project Objectives

1. Explore the use of generative AI in legal document preparation.
2. Integrate Google's Gemini API into a Python application.
3. Provide an interactive interface through Streamlit.
4. Use FastAPI as the backend API layer.
5. Demonstrate communication between frontend, backend and AI components.
6. Explore the practical application of AI-assisted text generation.

## Key Features

### 1. AI-Powered Document Generation

The application uses Google's Gemini API to generate document content based on information provided through the application interface.

### 2. Interactive User Interface

The Streamlit frontend provides an interface for entering the required information and interacting with the document generation workflow.

### 3. Backend API Integration

FastAPI provides the backend layer for handling application requests and connecting the frontend workflow with the relevant application components.

### 4. Generative AI Integration

The Gemini integration enables AI-assisted text generation as part of the document preparation process.

### 5. Python-Based Architecture

The application uses separate frontend, backend and AI-related directories to organize its components.

---

## Application Architecture

LegalEase is organized around three primary application components:

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | Streamlit | User interaction and input interface |
| Backend | FastAPI | API request handling |
| AI Integration | Google Gemini API | AI-assisted document generation |

### High-Level Workflow

```text
        USER
          |
          v
   STREAMLIT FRONTEND
          |
          v
     FASTAPI BACKEND
          |
          v
    AI INTEGRATION
          |
          v
    GEMINI API
          |
          v
  GENERATED DOCUMENT
          |
          v
    USER INTERFACE
```

The frontend collects user input, the backend handles the application request, and the AI integration communicates with Gemini to generate document content.

---

## Technology Stack

### Programming Language
- Python

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Artificial Intelligence
- Google Gemini API
- Generative AI

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Python Virtual Environment

---

## Project Structure

```text
LegalEase/
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
│   └── app.py
│
├── legalEaseAPI/
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

The project is organized into separate directories for the user interface, backend API and AI-related functionality.

*Note: The structure above is a simplified representation. Refer to the repository for the complete directory contents.*

---

## Application Workflow

The application follows a sequence of steps:

1. The user opens the Streamlit application.
2. The user enters the information requested by the interface.
3. The application initiates the document generation workflow.
4. The backend handles the relevant request.
5. The AI integration communicates with Google's Gemini API.
6. Gemini generates document content based on the supplied information.
7. The generated output is presented through the application interface.

---

## Installation and Setup

### Prerequisites

Ensure the following are installed:

- Python 3
- pip package manager
- Git
- Google Gemini API key

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

### Step 3: Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure the API Key

Create a `.env` file in the location expected by the application and configure your Gemini API key using the variable name referenced in the source code.

Do not upload API keys or other credentials to GitHub.

---

## Running the Application

LegalEase uses separate commands for starting the backend and frontend.

### Start the FastAPI Backend

Open a terminal in the application directory and execute:

```bash
uvicorn legalEaseAPI.main:app --reload
```

The backend will start using Uvicorn.

### Start the Streamlit Frontend

Open a second terminal in the same application directory and execute:

```bash
streamlit run frontend/app.py
```

Streamlit will provide a local browser URL.

Open the displayed URL to access the application.

---

## Potential Use Cases

The project explores possible applications of generative AI in:

- Drafting structured legal document content.
- Simplifying initial document preparation.
- Assisting users with formal document language.
- Exploring AI-powered document workflows.
- Demonstrating API-based integration of generative AI services.

These are potential application areas, not a claim that the system supports every category of legal document.

---

## Limitations

- Generated content depends on the quality and completeness of user input.
- AI-generated legal text may contain inaccuracies or omissions.
- The application does not independently verify legal validity.
- Output quality may vary depending on the AI model response.
- A valid Gemini API key and internet connection are required for AI generation.
- The prototype should not be treated as a substitute for qualified legal advice.

---

## Future Improvements

Possible areas for further development include:

- Additional document templates.
- Improved input validation.
- Document export options such as PDF and DOCX.
- Better error handling and API response management.
- Document history and retrieval.
- Enhanced privacy and security controls.
- More comprehensive testing and validation.

---

## Development Note

LegalEase is an AI-assisted software project. AI-generated code assistance was used in its implementation, and the project serves as a practical exploration of integrating generative AI with frontend and backend application components.

---

## Disclaimer

LegalEase is an educational prototype intended to demonstrate the use of generative AI in document preparation.

It does not provide professional legal advice, establish an attorney-client relationship or guarantee the legal validity of generated documents.

All generated content should be reviewed by a qualified legal professional before being used for actual legal purposes.

---

## Repository

**GitHub:** https://github.com/shreyakannappan4-pixel/LegalEase
