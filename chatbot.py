import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import preprocess_text


# Load FAQ data
with open("data/faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Create a list of all questions and examples
all_questions = []
faq_indices = []

for index, faq in enumerate(faqs):
    # Add the main question
    all_questions.append(faq["question"])
    faq_indices.append(index)

    # Add example questions if available
    for example in faq.get("examples", []):
        all_questions.append(example)
        faq_indices.append(index)


# Preprocess all questions and examples
processed_questions = [
    preprocess_text(question)
    for question in all_questions
]


# Convert questions into TF-IDF vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)


def get_answer(user_question):
    # Preprocess user's question
    processed_user_question = preprocess_text(user_question)

    # Convert user's question into a TF-IDF vector
    user_vector = vectorizer.transform([processed_user_question])

    # Calculate cosine similarity
    similarities = cosine_similarity(
        user_vector,
        question_vectors
    )

    # Find the most similar question/example
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    # Minimum similarity threshold
    if best_score < 0.25:
        return "Sorry, I couldn't understand your question. Please ask something related to AI or Machine Learning."

    # Find which FAQ the matched example belongs to
    faq_index = faq_indices[best_match_index]

    return faqs[faq_index]["answer"]