import os

from flask import Flask, send_file
from app import app

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, World!'

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def main():
    app.run(port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    main()
