from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# create flask instance
app = Flask(__name__)
# create API instance
api = Api(app)
# create SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemy mapper
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    squad = db.Column(db.String(80), nullable=False)
    mp = db.Column(db.Integer, nullable=False)
    w = db.Column(db.Integer, nullable=False)
    d = db.Column(db.Integer, nullable=False)
    l = db.Column(db.Integer, nullable=False)
    gf = db.Column(db.Integer, nullable=False)
    ga = db.Column(db.Integer, nullable=False)
    gd = db.Column(db.String(80), nullable=False)
    pts = db.Column(db.Integer, nullable=False)
    pts_per_match = db.Column(db.Integer, nullable=False)
    x_goals = db.Column(db.Float(5), nullable=False)
    x_goals_allowed = db.Column(db.Float(5), nullable=False)
    x_gd = db.Column(db.String(80), nullable=False)
    x_gd_per_match = db.Column(db.String(80), nullable=False)
    last_five = db.Column(db.String(80), nullable=False)
    attendance = db.Column(db.String(80), nullable=False)
    top_team_scorer = db.Column(db.String(80), nullable=False)
    goalkeeper = db.Column(db.String(80), nullable=False)

    def __repre__(self):
        return f"{self.rank} - {self.team}"

# For GET request to http://localhost:5000/
class GetTeamRank(Resource):
    def get(self):
        teams = Team.query.all()
        team_list = []
        for team in teams:
            team_data = {'Squad': team.squad, 
                        'Rank': team.rank}
            team_list.append(team_data)
        return {"Team Ranks": team_list}, 200
    
api.add_resource(GetTeamRank, '/')

if __name__ == '__main__':
    app.run(debug=True)