import os

import requests
import streamlit as st

from formatters import (
    LOGO_PATH,
    format_docx,
    format_html_preview,
    format_pdf,
    sanitize_text,
)

API_URL = "http://localhost:8000/generate"

st.set_page_config(page_title="LegalEase", layout="centered")

# ---- Logo + title ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

# ---- Inputs ----
document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA)")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

# ---- Generate ----
if st.button("Generate Document"):
    if not (document_type.strip() and parties.strip() and terms.strip() and dates.strip()):
        st.warning("Please fill in all four fields.")
    else:
        with st.spinner("Writing your document..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates,
                    },
                    timeout=180,
                )
                if response.status_code == 200:
                    st.session_state.generated_text = sanitize_text(response.json()["document"])
                    st.session_state.doc_type = document_type
                    st.session_state.terms = terms
                    st.session_state.show_edit = False
                else:
                    st.error(f"Backend error: {response.json().get('detail', response.text)}")
            except requests.exceptions.ConnectionError:
                st.error("Cannot reach the backend. Start it first with: uvicorn legalEaseAPI.main:app --reload")
            except requests.exceptions.Timeout:
                st.error("The request took too long. Please try again.")

# ---- Preview / Edit / Download ----
if "generated_text" in st.session_state:
    st.success("Document Generated Successfully!")

    styled_html = format_html_preview(st.session_state.generated_text)
    st.markdown(
        "<div style='background:#111827;color:#e5e7eb;padding:20px;border-radius:10px;"
        f"max-height:350px;overflow-y:auto;'>{styled_html}</div>",
        unsafe_allow_html=True,
    )

    if st.button("\u270f\ufe0f Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.get("show_edit", False)

    if st.session_state.get("show_edit"):
        edited_text = st.text_area("Edit Document Below:", st.session_state.generated_text, height=300)
        st.session_state.generated_text = edited_text

    text = st.session_state.generated_text
    doc_type = st.session_state.doc_type
    file_stub = doc_type.strip().replace(" ", "_").lower() or "document"

    st.download_button("\U0001F4C4 Download as .TXT", data=text, file_name=f"{file_stub}.txt", mime="text/plain")
    st.download_button(
        "\U0001F4DD Download as .DOCX",
        data=format_docx(text, doc_type, st.session_state.get("terms", "")),
        file_name=f"{file_stub}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    st.download_button(
        "\U0001F4D5 Download as .PDF",
        data=format_pdf(text, doc_type),
        file_name=f"{file_stub}.pdf",
        mime="application/pdf",
    )
else:
    st.info("Click 'Generate Document' to start")
