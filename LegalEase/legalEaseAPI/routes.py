from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
_generator = None


def get_generator():
    """Create the Gemini 'chef' only once, the first time it is needed."""
    global _generator
    if _generator is None:
        _generator = GeminiDocumentGenerator()
    return _generator


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    try:
        response = get_generator().generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates,
        )
    except ValueError as e:  # missing API key
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:  # anything else from Gemini
        raise HTTPException(status_code=502, detail=f"Gemini error: {e}")
    return {"document": response}
