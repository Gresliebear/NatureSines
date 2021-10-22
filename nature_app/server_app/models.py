from server_app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

# ORM object relaiton mapping
# Create our database model
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False )
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True)

    # what is this below??
    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

class GuestDatatable(db.Model):
    __tablename__ = "guestdatatable"
    id = db.Column(db.Integer, primary_key=True)
    date_uploaded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    username = db.Column(db.String(30), unique=False, nullable=False )
    password = db.Column(db.String(60), nullable=False)
    audio = db.Column(db.LargeBinary, nullable=False)
    
    def __repr__(self):
        return f"GuestDatatable('{self.date_uploaded}')"