import requests
from bs4 import BeautifulSoup

URL = "https://www.premierleague.com/stats"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")