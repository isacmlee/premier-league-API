# Premier League API
#### Table of Contents
* [Introduction](#introduction)
* [Endpoints](#endpoints)  

### Introduction
This is a Basic Python REST API for Premier League Stats (2022 - 2023 Season) as of 4/12/23. 

Using BeautifulSoup, I scraped Premier League data from fbref.com. I then added the scraped data into a SQLAlchemy database that can be accessed or modified with 4 HTTP methods (GET, POST, PUT, DELETE). There are a total of 6 endpoints (3 GETS, 1 POST, 1 PUT, 1 DELETE). 


<b>Tools Used</b>: <i>Python, BeautifulSoup, Requests, Pandas, Flask, Flask-RESTful, Flask-SQLAlchemy</i>

### Endpoints
#### GET /team_ranks
Retrieve ranks for all Teams in the Premier League.
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
Retrieve match stats for specified Team in the Premier League.
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
Retrieve top scorer for all Teams in the Premier League.
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
requests.get(http://127.0.0.1:5000/add_team)
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
