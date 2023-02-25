from flask import Flask
from home.views import home_view
from flask_sqlalchemy import SQLAlchemy
from api import *
import os


app = Flask(__name__)  # Create application object
# Configure application with settings file, not strictly necessary
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'

db = SQLAlchemy(app)

# Register url's so application knows what to do


@app.route('/')
def index():
    try:
        db.session.execute('SELECT 1')
        return 'Database connection successful!'
    except:
        return 'Database connection failed!'


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


if __name__ == '__main__':
    app.run(debug=True)  # Run our application
