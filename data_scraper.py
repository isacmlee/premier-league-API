import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send HTTP Request 
URL = "https://fbref.com/en/comps/9/Premier-League-Stats"
page = requests.get(URL)

# BeautifulSoup parses html_source
soup = BeautifulSoup(page.text, "html.parser")

# Scrape PL Table column names 
th_cols = soup.find_all("thead")[0].find_all("th")
col_names = []
for i in th_cols:
    col_names.append(i.text)

# Scrape PL Table values 
tr_teams = soup.find_all("tbody")[0].find_all("tr")

# For each team, iterate through the tds
table_values = []
for tr in tr_teams: 
    row_values = []
    tds = tr.findChildren(recursive=False)
    for td in tds:
        row_values.append(td.text)
    table_values.append(row_values)

pl_table = pd.DataFrame(data=table_values,columns=col_names)
pl_table.drop(columns=['Notes'],inplace=True)
pl_table.to_csv("data/pl_table.csv",index=False)
