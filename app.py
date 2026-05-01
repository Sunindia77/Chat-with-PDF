import streamlit as st
from rag import process_pdf, get_answer
from llm import ask_llm
import tempfile

st.title("📄 Chat with PDF")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    vector_store = process_pdf(file_path)

    query = st.text_input("Ask a question:")

    if query:
        with st.spinner("Thinking..."):
            context = get_answer(vector_store, query)
            answer = ask_llm(context, query)

        st.subheader("💡 Answer")
        st.write(answer)