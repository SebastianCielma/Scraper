import requests
import random
import time
from bs4 import BeautifulSoup
from requests import RequestException


class Scraper:
    def __init__(self):
        self.base_url = "https://www.rbc.ru"
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",

        ]
        self.proxies = [
            "http://your_proxy_address1",
            "http://your_proxy_address2",

        ]

    def scrape_articles(self, keywords):
        articles = []
        for keyword in keywords:
            url = f"{self.base_url}/search/?query={keyword}"
            headers = {
                "User-Agent": random.choice(self.user_agents),

            }
            proxy = random.choice(self.proxies)
            try:
                response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    article_tags = soup.find_all("a", class_="search-item")
                    for article_tag in article_tags:
                        title = article_tag.text.strip()
                        article_url = article_tag["href"]
                        article_response = requests.get(article_url, headers=headers,
                                                        proxies={"http": proxy, "https": proxy})
                        if article_response.status_code == 200:
                            article_soup = BeautifulSoup(article_response.text, 'html.parser')
                            date = article_soup.find("span", class_="article__header__date").text.strip()
                            author = article_soup.find("span",
                                                       class_="article__author").text.strip() if article_soup.find(
                                "span", class_="article__author") else None
                            content = article_soup.find("div", class_="article__text").text.strip()
                            articles.append({
                                "title": title,
                                "date": date,
                                "author": author,
                                "content": content
                            })
                        time.sleep(random.uniform(1, 3))
            except RequestException as e:
                print(f"Error while fetching article: {e}")
            except RequestException as e:
                print(f"Error while fetching search results: {e}")
            return articles




