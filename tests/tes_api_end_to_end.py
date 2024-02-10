import requests
import unittest

class TestAPIEndToEnd(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000"
        self.api_url = f"{self.base_url}/add_keyword"
        self.articles_url = f"{self.base_url}/articles"

    def test_add_keyword_and_get_articles(self):
        data = {"keyword": "test_keyword"}
        response = requests.post(self.api_url, json=data)
        self.assertEqual(response.status_code, 201)

        response = requests.get(self.articles_url)
        self.assertEqual(response.status_code, 200)
        articles = response.json()
        self.assertTrue(isinstance(articles, list))
        self.assertTrue(len(articles) > 0)

if __name__ == '__main__':
    unittest.main()
