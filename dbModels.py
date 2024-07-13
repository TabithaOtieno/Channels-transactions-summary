from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pesalink(db.Model):
    __tablename__ = 'pesalink'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    # transaction time

class Card(db.Model):
    __tablename__ = 'powercard'
    id = db.Column(db.Integer, primary_key=True)
    p_action = db.Column(db.String(50), nullable=False)

class Whizz(db.Model):
    __tablename__ = 'whizztransactions'
    id = db.Column(db.Integer, primary_key=True)
    recipient_status = db.Column(db.String(50), nullable=False)
