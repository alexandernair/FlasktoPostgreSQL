from flask import Flask
from home.views import home_view
from flask_sqlalchemy import SQLAlchemy
from api import *
import os


app = Flask(__name__)  # Create application object
# Configure application with settings file, not strictly necessary
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://localhost/mydatabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Register url's so application knows what to do
app.register_blueprint(home_view)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)  # Run our application
