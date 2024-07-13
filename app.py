from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from appUrls import *

app = Flask(__name__)

# Configure the PostgreSQL Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:cozlin@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
