import finnhub


def scrape_news():
    finnhub_client = finnhub.Client(api_key="")

    news = finnhub_client.general_news('general', min_id=0)

    return news
