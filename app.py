
import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Movie Review Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "sentiment_model.pkl")
tfidf = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")

st.markdown(
    "<h2 style='white-space: nowrap;'>🎬 Movie Review Sentiment Analyzer</h2>",
    unsafe_allow_html=True
)

st.write("Enter a movie review to predict its sentiment.")

review = st.text_area(
    "Your movie review",
    placeholder="Write your review here...",
    height=120
)

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        review_tfidf = tfidf.transform([review])
        prediction = model.predict(review_tfidf)[0]

        if prediction == "positive":
            st.success("😊 Positive Review")
        elif prediction == "negative":
            st.error("😞 Negative Review")
