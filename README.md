# News Summarization & Sentiment Analysis with Hindi TTS

## Overview
This project is a **web-based application** that extracts key details from multiple news articles about a company, performs **sentiment analysis**, conducts **comparative analysis**, and generates **text-to-speech (TTS) output in Hindi**.

Users can **input a company name**, fetch related news, analyze sentiment, and listen to a summarized report in Hindi.

## Features
✅ **Web Scraping**: Fetch news articles using `BeautifulSoup`  
✅ **Sentiment Analysis**: Classify news as Positive, Negative, or Neutral  
✅ **Comparative Analysis**: Compare sentiment trends across articles  
✅ **Hindi Text-to-Speech**: Convert insights into Hindi speech using `gTTS`  
✅ **User-Friendly Web UI**: Built with `Streamlit`  
✅ **API-based Architecture**: Backend with `FastAPI`  
✅ **Deployed on Hugging Face Spaces**  

## Tech Stack
- **Python** (FastAPI, Streamlit, BeautifulSoup, gTTS, VADER, NLTK, Transformers)
- **Deployment**: Hugging Face Spaces

## Setup Instructions
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/news-summarization-tts.git
cd news-summarization-tts
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Backend (FastAPI)**
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

### **4️⃣ Run the Web UI (Streamlit)**
```bash
streamlit run app.py
```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/news/{company}` | Fetch news articles & sentiment analysis |
| **GET** | `/tts/?text=YOUR_TEXT` | Generate Hindi TTS audio |

## Expected Output Format
```json
{
    "Company": "Tesla",
    "Articles": [
        {"Title": "Tesla's Record Sales", "Sentiment": "Positive"},
        {"Title": "Tesla Faces Regulatory Issues", "Sentiment": "Negative"}
    ],
    "Final Sentiment Analysis": "Tesla’s news coverage is mixed",
    "Audio": "[Hindi Speech]"
}
```

## Deployment
🚀 **Hugging Face Spaces**: [Live Demo](https://huggingface.co/spaces/genuu/news-sentiment-tts)

## Contribution
Feel free to fork this repository and contribute improvements!

📌 **Author:** Genius Khunte  
📌 **GitHub:** [Your GitHub Profile](https://github.com/gen0014)

