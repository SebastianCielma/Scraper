import unittest
from scrapers.scraper import Scraper

class TestRBCScraper(unittest.TestCase):
    def setUp(self):
        self.proxies = ["http://proxy1", "http://proxy2"]
        self.user_agents = ["user_agent1", "user_agent2"]
        self.scraper = Scraper(self.proxies, self.user_agents)

    def test_scrape_articles_with_no_keywords(self):
        articles = self.scraper.scrape_articles()
        self.assertEqual(len(articles), 0)

    def test_scrape_articles_with_keywords(self):
        self.scraper.keywords = ["keyword1", "keyword2"]
        articles = self.scraper.scrape_articles()
        self.assertTrue(isinstance(articles, list))

if __name__ == '__main__':
    unittest.main()
