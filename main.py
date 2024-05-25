
import nltk
# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

from textblob import TextBlob
from newspaper import Article

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def index():
    return "Make request to /summarize with article URL"

@app.get("/summarize")
async def summarize(url: str):
    print(url)
    # Create the article object
    article = Article(url)
    # Grab the article and parse the data
    article.download()
    article.parse()
    # Run NLP Processes
    article.nlp()

    print(f'{article.title}')
    print(f'{article.authors}')
    print(f'{article.summary}')

    sentiment = TextBlob(article.text)
    print(f'Sentiment: {"Positive" if sentiment.polarity > 0 else "Negative" if sentiment.polarity < 0 else "Neutral"}')
    return article.summary

