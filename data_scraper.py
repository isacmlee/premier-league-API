import requests
from bs4 import BeautifulSoup

URL = "https://www.premierleague.com/stats"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mainContent")
results = results.find("div",class_="hasSideNav")
results = results.find("div",class_="sidebarPush")
results = results.find_all("div",class_="col-12")
stats = results[1].find_all("section",class_="mainWidget statsRow DashboardPlayerStats")
stats = stats[0].find("ul",class_="block-list-4 mobileScrollList")
children = stats.findChildren("li")
print(children)


# results = soup.find_all("div", class_="")
print(stats)