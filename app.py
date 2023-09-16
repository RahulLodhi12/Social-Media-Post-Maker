from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])

def index():
    # url = "https://www.cricbuzz.com/cricket-news/latest-news"
    url = "https://www.businesstoday.in/technology"

    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    # print(soup.find_all("div",class_="widget-listing-thumb",limit=10))
    # outerdata = soup.find_all("div",class_="cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container",limit=10)
    outerdata = soup.find_all("div",class_="widget-listing-thumb",limit=10)
    finalNews=""
    for data in outerdata:
        news = data.a.get("title")
        finalNews += "\u2022 " + news + "\n"
    return render_template("index.html",News=finalNews)