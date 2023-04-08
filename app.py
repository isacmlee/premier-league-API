from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# create flask instance
app = Flask(__name__)
# create API instance
api = Api(app)
# create SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemy mapper
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(80), nullable=False)
    matches = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    ties = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    goals_for = db.Column(db.Integer, nullable=False)
    goals_against = db.Column(db.Integer, nullable=False)
    goal_difference = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    points_per_match = db.Column(db.Integer, nullable=False)
