from app import *
import pandas as pd

teams = pd.read_csv("data/pl_table.csv")

app.app_context().push()

# Create database 
db.create_all()

# Add rows to db 
for i, row in teams.iterrows():
        team_row = Team(
            id=i,
            rank=row['Rk'],
            squad=row['Squad'],
            mp = row['MP'],
            w = row['W'],
            d = row['D'],
            l = row['L'],
            gf = row['GF'],
            ga = row['GA'],
            gd = row['GD'],
            pts = row['Pts'],
            pts_per_match = row['Pts/MP'],
            x_goals = row['xG'],
            x_goals_allowed = row['xGA'],
            x_gd = row['xGD'],
            x_gd_per_match = row['xGD/90'],
            last_five = row['Last 5'],
            attendance = row['Attendance'],
            top_team_scorer = row['Top Team Scorer'],
            goalkeeper = row['Goalkeeper']
        )
        db.session.add(team_row)
        db.session.commit()