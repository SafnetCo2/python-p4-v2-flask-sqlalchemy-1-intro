from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy object to represent the database
db = SQLAlchemy(app)

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# Define models
class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

class User(db.Model):
    __tablename__ = 'users'  # Changed table name to 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    species = db.Column(db.String)
    verified = db.Column(db.Boolean, default=False)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
