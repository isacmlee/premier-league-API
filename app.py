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

# GET request for all Teams' ranks
class GetTeamRank(Resource):
    def get(self):
        teams = Team.query.all()
        team_list = []
        for team in teams:
            team_data = {'Squad': team.squad, 
                        'Rank': team.rank}
            team_list.append(team_data)
        return {"Team Ranks": team_list}, 200

# GET request for specific Team's Stats
class GetTeamStats(Resource):
    def get(self,squad):
        team = Team.query.filter_by(squad=squad).first()
        if team is None:
            return {"Error": "Not Found"}, 40
        team_data = {'Squad': team.squad,
                        'Matches Played': team.mp,
                        'Wins': team.w,
                        'Ties': team.d,
                        'Losses': team.l}
        return {f"{squad} Match Stats": team_data}, 200

# GET request for Teams' top scorer 
class GetTeamTopScorer(Resource):
    def get(self):
        teams = Team.query.all()
        team_list = []
        for team in teams:
            team_data = {'Squad': team.squad,
                         'Top Scorer': team.top_team_scorer}
            team_list.append(team_data)
        return {"Team Top Scorers": team_list}, 200

# POST request to add new team to database
class AddTeam(Resource):
    def post(self):
        if request.is_json:
            team = Team(
                    rank=request.json['rank'],
                    squad=request.json['squad'],
                    mp=request.json['mp'],
                    w=request.json['w'],
                    d=request.json['d'],
                    l=request.json['l'],
                    gf=request.json['gf'],
                    ga=request.json['ga'],
                    gd=request.json['gd'],
                    pts=request.json['pts'],
                    pts_per_match=request.json['pts_per_match'],
                    x_goals=request.json['x_goals'],
                    x_goals_allowed=request.json['x_goals_allowed'],
                    x_gd=request.json['x_gd'],
                    x_gd_per_match=request.json['x_gd_per_match'],
                    last_five=request.json['last_five'],
                    attendance=request.json['attendance'],
                    top_team_scorer=request.json['top_team_scorer'],
                    goalkeeper=request.json['goalkeeper']
            )
            db.session.add(team)
            db.session.commit()
            # return a json response
            return make_response(jsonify({'ID': team.id,'Squad':team.squad}), 201)
        else:
            return {'Error': 'Request must be JSON'}, 400

# PUT request to update Team Name 
class UpdateTeamName(Resource):
    def put(self,squad):
        if request.is_json:
            team = Team.query.filter_by(squad=squad).first()
            if team is None:
                return {'Error': 'Not Found'}, 404 
            else:
                team.squad = request.json['squad']
                db.session.commit()
                return 'Updated Team Name', 200
        else:
            return {'Error': 'Request must be JSON'}, 400
        
# DELETE request for delete Team
class DeleteTeam(Resource):
    def delete(self,squad):
        team = Team.query.filter_by(squad=squad).first()
        if team is None:
            return {'Error': 'Not Found'}, 404 
        db.session.delete(team)
        db.session.commit()
        return f'{squad} is deleted', 200

# Adds resource to API
api.add_resource(GetTeamRank, '/team_rank') # Get all Team Names and Ranks
api.add_resource(GetTeamStats, '/team_stats/<squad>') # Get Squad Stats
api.add_resource(GetTeamTopScorer, '/team_top_scorer') # Get Top Scorer for all Teams
api.add_resource(AddTeam,'/add_team') # Add new team
api.add_resource(UpdateTeamName,'/update_team_name/<squad>') # Update Team Name 
api.add_resource(DeleteTeam,'/delete_team/<squad>')

if __name__ == '__main__':
    app.run(debug=True)