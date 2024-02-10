from flask import Flask
from api.rest_api import API
from scrapers.scraper import Scraper

app = Flask(__name__)

def main():
    proxies = [
        "http://your_proxy_address1",
        "http://your_proxy_address2",

    ]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",

    ]

    scraper = Scraper(proxies, user_agents)
    api = API(scraper)
    api.run(debug=True)

if __name__ == "__main__":
    main()
