
# main.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    data = {}
    data['title'] = soup.title.string
    data['paragraphs'] = [p.text for p in soup.find_all('p')]
    return jsonify(data)

@app.route('/result')
def result():
    data = request.args.get('data')
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
