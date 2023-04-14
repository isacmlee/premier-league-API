# Premier League API
#### Table of Contents
* [Introduction](#introduction)
* [Installation](#installation)
* [Endpoints](#endpoints)  

### Introduction
This is a Basic Python REST API for Premier League Stats (2022 - 2023 Season) as of 4/12/23. 

Using BeautifulSoup, I scraped Premier League data from fbref.com. I then added the scraped data into a SQLAlchemy database that can be accessed or modified with 4 HTTP methods (GET, POST, PUT, DELETE). There are a total of 6 endpoints (3 GETS, 1 POST, 1 PUT, 1 DELETE). 

#### Directory Structure
```
├── data
│   ├── pl_table.csv       <- Premier League data scraped using BeautifulSoup.
|
├── instance               <- Holds Flask configuration files.
│   ├── teams_db.db        <- SQLAlchemy database for pl_table.csv.
|
├── .gitignore             <- Specifies intentionally untracked files that Git should ignore.
├── app.py                 <- Flask Application root. 
├── create_database.py     <- Python script to add pl_table.csv to SQLAlchemy database.
├── data_scraper.py        <- Python script that uses BeautifulSoup to scrape Premier League data.
├── README.md              <- The README for users.
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                          generated with `pip freeze > requirements.txt`
```
<b>Tools Used</b>: <i>Python, BeautifulSoup, Requests, Pandas, Flask, Flask-RESTful, Flask-SQLAlchemy</i>

### Installation

### Endpoints
* [GET /team_ranks](#get-team_ranks)
* [GET /team_stats/< squad >](#get-team_stats-squad-)  
* [GET /team_top_scorer](#get-team_top_scorer)
* [POST /add_team](#post-add_team)
* [PUT /update_team_name/< squad >](#put-update_team_name-squad-)
* [DELETE /delete_team/< squad >](#delete-delete_team-squad-)

#### GET /team_ranks
Retrieve ranks for all Teams in the Premier League database.
``` python 
# Request
requests.get(http://127.0.0.1:5000/team_ranks)
```
``` python
# Response
{
    "Team Ranks": [
        {
            "Squad": "Arsenal",
            "Rank": 1
        },
        {
            "Squad": "Manchester City",
            "Rank": 2
        },
        {
            "Squad": "Newcastle Utd",
            "Rank": 3
        },
        {
            "Squad": "Manchester Utd",
            "Rank": 4
        },
        {
            "Squad": "Tottenham",
            "Rank": 5
        },
        {
            "Squad": "Aston Villa",
            "Rank": 6
        },
        {
            "Squad": "Brighton",
            "Rank": 7
        },
        {
            "Squad": "Liverpool",
            "Rank": 8
        },
        {
            "Squad": "Brentford",
            "Rank": 9
        },
        {
            "Squad": "Fulham",
            "Rank": 10
        },
        {
            "Squad": "Chelsea",
            "Rank": 11
        },
        {
            "Squad": "Crystal Palace",
            "Rank": 12
        },
        {
            "Squad": "Wolves",
            "Rank": 13
        },
        {
            "Squad": "West Ham",
            "Rank": 14
        },
        {
            "Squad": "Bournemouth",
            "Rank": 15
        },
        {
            "Squad": "Leeds United",
            "Rank": 16
        },
        {
            "Squad": "Everton",
            "Rank": 17
        },
        {
            "Squad": "Nott'ham Forest",
            "Rank": 18
        },
        {
            "Squad": "Leicester City",
            "Rank": 19
        },
        {
            "Squad": "Southampton",
            "Rank": 20
        }
    ]
}
```
#### GET /team_stats/< squad >
Retrieve match stats for specified Team in the Premier League database.
``` python 
# Request
requests.get(http://127.0.0.1:5000/team_stats/Liverpool)
```
``` python
# Response
{
    "Liverpool Match Stats": {
        "Squad": "Liverpool",
        "Matches Played": 29,
        "Wins": 12,
        "Ties": 8,
        "Losses": 9
    }
}
```
#### GET /team_top_scorer
Retrieve top scorer for all Teams in the Premier League database.
``` python 
# Request
requests.get(http://127.0.0.1:5000/team_top_scorer)
```
``` python
# Response
{
    "Team Top Scorers": [
        {
            "Squad": "Arsenal",
            "Top Scorer": "Martinelli - 14"
        },
        {
            "Squad": "Manchester City",
            "Top Scorer": "Erling Haaland - 30"
        },
        {
            "Squad": "Newcastle Utd",
            "Top Scorer": "Miguel Almirón - 11"
        },
        {
            "Squad": "Manchester Utd",
            "Top Scorer": "Marcus Rashford - 15"
        },
        {
            "Squad": "Tottenham",
            "Top Scorer": "Harry Kane - 23"
        },
        {
            "Squad": "Aston Villa",
            "Top Scorer": "Ollie Watkins - 12"
        },
        {
            "Squad": "Brighton",
            "Top Scorer": "Alexis Mac Allister - 8"
        },
        {
            "Squad": "Liverpool",
            "Top Scorer": "Mohamed Salah - 13"
        },
        {
            "Squad": "Brentford",
            "Top Scorer": "Ivan Toney - 18"
        },
        {
            "Squad": "Fulham",
            "Top Scorer": "Aleksandar Mitrović - 11"
        },
        {
            "Squad": "Chelsea",
            "Top Scorer": "Kai Havertz - 7"
        },
        {
            "Squad": "Crystal Palace",
            "Top Scorer": "Wilfried Zaha - 6"
        },
        {
            "Squad": "Wolves",
            "Top Scorer": "Daniel Podence - 6"
        },
        {
            "Squad": "West Ham",
            "Top Scorer": "Saïd Benrahma, Jarrod Bowen - 4"
        },
        {
            "Squad": "Bournemouth",
            "Top Scorer": "Philip Billing - 7"
        },
        {
            "Squad": "Leeds United",
            "Top Scorer": "Rodrigo - 11"
        },
        {
            "Squad": "Everton",
            "Top Scorer": "Demarai Gray - 4"
        },
        {
            "Squad": "Nott'ham Forest",
            "Top Scorer": "Brennan Johnson - 8"
        },
        {
            "Squad": "Leicester City",
            "Top Scorer": "Harvey Barnes - 10"
        },
        {
            "Squad": "Southampton",
            "Top Scorer": "James Ward-Prowse - 7"
        }
    ]
}
```
#### POST /add_team
Add new Team to the Premier League database. 
``` python 
# Request
URL = "http://127.0.0.1:5000/add_team"

body = {
    "rank": 21,
    "squad": "Loserpool FC",
    "mp": 25,
    "w": 17,
    "d": 3,
    "l": 5,
    "gf": 56,
    "ga": 5,
    "gd": 51,
    "pts": 75,
    "pts_per_match": 45,
    "x_goals": 3.42,
    "x_goals_allowed": 0.032,
    "x_gd": 122,
    "x_gd_per_match": 34,
    "last_five": "W W W W W",
    "attendance": "23,232",
    "top_team_scorer": "Isac Lee",
    "goalkeeper": "John Cena"
}
 
response = requests.post(URL, json=body)
```
``` python
# Response
{
    "ID": 20,
    "Squad": "Loserpool FC"
}
```
#### PUT /update_team_name/< squad >
Update Team name for specified Team in the Premier League database.
``` python 
# Request
URL = "http://127.0.0.1:5000/update_team_name/Loserpool FC"

body = {
    "squad": "Winnerpool"
}

response = requests.put(URL, json=body)
```
``` python
# Response
"Updated Team Name"
```
#### DELETE /delete_team/< squad >
Delete specified Team in the Premier League database.
``` python 
# Request
requests.delete("http://127.0.0.1:5000/update_team_name/Loserpool FC")
```
``` python
# Response
"Loserpool FC is deleted"
```


