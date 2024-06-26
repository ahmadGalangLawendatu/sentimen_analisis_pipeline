import finnhub


def scrape_news():
    finnhub_client = finnhub.Client(api_key="cprs6q1r01qh73o03jqgcprs6q1r01qh73o03jr0")

    news = finnhub_client.general_news('general', min_id=0)

    return news
