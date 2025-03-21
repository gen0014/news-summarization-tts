import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("News Sentiment Analyzer & Hindi TTS")

company = st.text_input("Enter Company Name")

if st.button("Analyze News"):
    response = requests.get(f"{API_URL}/news/{company}").json()
    st.json(response)

    # Play Hindi Audio
    hindi_text = response["sentiment_report"]["Insights"][0]
    requests.get(f"{API_URL}/tts/?text={hindi_text}")
    st.audio("output.mp3")
