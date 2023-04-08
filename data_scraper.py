import requests
from selenium import webdriver 
from bs4 import BeautifulSoup

# using selenium to grab JS rendered data
browser = webdriver.Chrome()
browser.get("https://www.premierleague.com/stats")
html_source = browser.page_source
browser.quit()

# BeautifulSoup parses html_source
soup = BeautifulSoup(html_source, "html.parser")

results = soup.find(id="mainContent")
results = results.find("div",class_="hasSideNav")
results = results.find("div",class_="sidebarPush")
results = results.find_all("div",class_="col-12")
stats = results[1].find("section",class_="mainWidget statsRow DashboardPlayerStats")
stats = stats[0].find("ul",class_="block-list-4 mobileScrollList")
children = stats.findChildren("li")
print(children)


# results = soup.find_all("div", class_="")
