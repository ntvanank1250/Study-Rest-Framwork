from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy


#create an instance of the flask app
app=Flask(__name__)

#configure our Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False