from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from scrapers.scraper import Scraper

app = Flask(__name__)
auth = HTTPBasicAuth()

# Simple dictionary of users and passwords for authentication
users = {
    "admin": "password"
}

# Simple authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

class API:
    def __init__(self, rbc_scraper):
        self.rbc_scraper = rbc_scraper

    @app.route('/add_keyword', methods=['POST'])
    @auth.login_required
    def add_keyword(self):
        data = request.get_json()
        keyword = data.get('keyword')
        if not keyword:
            return jsonify({"error": "Keyword missing in request."}), 400

        self.rbc_scraper.keywords.append(keyword)
        return jsonify({"message": f"Keyword '{keyword}' added successfully."}), 201

    @app.route('/articles', methods=['GET'])
    @auth.login_required
    def get_articles(self):
        try:
            articles = self.rbc_scraper.scrape_articles()
            return jsonify(articles)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
