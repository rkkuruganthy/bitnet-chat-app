# app.py
import streamlit as st
import requests

API_URL = "http://localhost:8000/generate"

st.set_page_config(page_title="BitNet Chat (Local)", layout="centered")
st.title("🤖 BitNet Chat Assistant (Offline)")

# Input area
prompt = st.text_area("Enter your prompt", height=150)
max_tokens = st.slider("Max Tokens", 50, 400, 200)

if st.button("Submit"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Waiting for response from local model..."):
            try:
                response = requests.post(API_URL, json={
                    "prompt": prompt,
                    "max_tokens": max_tokens
                })

                if response.status_code == 200:
                    result = response.json()
                    st.success("Response received:")
                    st.text_area("Model Response", result.get("response", ""), height=300)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("❌ Failed to connect to FastAPI backend. Is it running on port 8000?")
