import requests
import unittest

class TestAPIIntegration(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000"
        self.api_url = f"{self.base_url}/add_keyword"
        self.articles_url = f"{self.base_url}/articles"

    def test_add_keyword(self):
        data = {"keyword": "test_keyword"}
        response = requests.post(self.api_url, json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_articles(self):
        response = requests.get(self.articles_url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
