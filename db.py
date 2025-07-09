from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  

db = SQLAlchemy()

def init_db(app):
    user = os.getenv('DB_USER', 'postgres')
    password = os.getenv('DB_PASSWORD', 'asdf')
    host = os.getenv('DB_HOST', 'localhost')
    port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'parkingAPI')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

class ParkingSlot(db.Model):
    __tablename__ = 'parking_slots'
    id = db.Column(db.Integer, primary_key=True)
    is_occupied = db.Column(db.Boolean, default=False)
    reserved_for = db.Column(db.String(100), nullable=True)
    slot_type = db.Column(db.String(50), default='general')

class ParkingSession(db.Model):
    __tablename__ = 'parking_sessions'
    id = db.Column(db.Integer, primary_key=True)
    slot_id = db.Column(db.Integer, db.ForeignKey('parking_slots.id', ondelete='CASCADE'))
    started_at = db.Column(db.DateTime, server_default=db.func.now())
    ended_at = db.Column(db.DateTime, nullable=True)
