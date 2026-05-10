import sys
import os

# FORCE the venv to be the #1 priority in the Python Path
venv_site_packages = os.path.join(os.getcwd(), 'venv', 'lib', 'python3.10', 'site-packages')
sys.path.insert(0, venv_site_packages)

import torch
import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

st.set_page_config(page_title="Software Translator", page_icon="💻")

@st.cache_resource
def load_assets():
    model_path = "." 
    tokenizer = MarianTokenizer.from_pretrained(model_path)
    model = MarianMTModel.from_pretrained(model_path)
    return tokenizer, model

st.title("💻 Software Domain AI")

try:
    tokenizer, model = load_assets()
    st.success("✅ PyTorch Handshake Successful!")
    
    user_input = st.text_area("English Source:", "The application crashed due to a memory leak.")

    if st.button("Translate"):
        inputs = tokenizer(user_input, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(**inputs)
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.info(f"**Dutch:** {translation}")

except Exception as e:
    st.error(f"⚠️ Handshake Error: {e}")
    st.write("Current Priority Path:", sys.path[0])
