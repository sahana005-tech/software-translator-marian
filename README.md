# 💻 Software-Specific Neural Machine Translation (NMT)

A specialized translation application built with a fine-tuned **MarianMT** transformer model. This system is engineered to translate technical software engineering terminology from English to Dutch with high contextual accuracy.

## 🚀 Key Technical Features
- **Domain-Specific Fine-Tuning**: Optimized for software engineering vernacular (e.g., "asynchronous callbacks," "null pointers," "git commits").
- **100% Local Inference**: Engineered for data privacy and security; no external API calls are made during translation.
- **Optimized for Intel i9**: Configured with specialized dependency management to handle PyTorch/NumPy versioning on x86_64 macOS architectures.
- **Secure Implementation**: Utilizes the `safetensors` format for model weights to ensure safe and fast loading.

## 🛠️ Tech Stack
- **Model Architecture**: MarianMT (Hugging Face Transformers)
- **UI Framework**: Streamlit
- **Language**: Python 3.10
- **Environment**: Virtual Environment (venv) with isolated dependency mapping.

## 📦 Installation & Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sahana005-tech/software-translator-marian.git
   cd software-translator-marian
   ```

2. **Set up the environment**:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## 🛡️ Data Privacy
This project follows **Secure AI Implementation** principles. All data processing occurs locally on the user's hardware, making it suitable for translating proprietary code documentation without risking data exposure to third-party LLM providers.
