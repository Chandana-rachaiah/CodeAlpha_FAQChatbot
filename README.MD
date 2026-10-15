# AI-Based FAQ Chatbot

## Project Description
This project is an AI-based FAQ chatbot that answers frequently asked questions related to Artificial Intelligence and Machine Learning. It uses TF-IDF vectorization and cosine similarity to identify the most relevant question and return its corresponding answer.

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- NLTK
- TF-IDF Vectorization
- Cosine Similarity

## Features
- Answers frequently asked questions about AI and Machine Learning.
- Recognizes alternative phrasings of selected questions.
- Uses text preprocessing to improve question matching.
- Displays a fallback response for unrelated questions.
- Provides a simple web interface using Streamlit.

## Project Structure
- `app.py` — Streamlit web interface
- `chatbot.py` — FAQ matching and answer selection
- `preprocessing.py` — Text preprocessing
- `data/faqs.json` — FAQ questions and answers
- `.gitignore` — Excludes unnecessary files

## How to Run
1. Install Python.
2. Install the required libraries: `streamlit`, `scikit-learn`, and `nltk`.
3. Ensure the NLTK English stopwords data is available.
4. Run the application with:

   `python -m streamlit run app.py`

5. Open the local URL displayed in the terminal.

## Project Purpose
This project demonstrates basic natural language processing and information retrieval techniques for answering frequently asked questions.
