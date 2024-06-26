import mongodb_loader
import pandas as pd
from sentiment_analysis import SentimentAnalysis
import postgres_loader


def run():
    # Mendapatkan akses ke koleksi 'Finnhub_news' dari MongoDB
    db = mongodb_loader.get_data("news", "Finnhub_news")

    # Mencetak semua dokumen dalam koleksi 'Finnhub_news'
    news = [doc for doc in db.find()]
    print(news)

    output = []
    for news_summary in news:
        output.append(SentimentAnalysis(text=news_summary["summary"]).execute())

        print(f"Summary {news_summary['summary']} successfully analized")

    sentiment_output = pd.DataFrame(output)

    postgres_loader.load(sentiment_output, "sentiment_news_analysis")

    print("Successfully loaded to Postgres")
