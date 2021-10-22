from flask import render_template, current_app, redirect, url_for, request, session, jsonify
from . import bp
import os
import time
import pickle
from server_app import db, bcrypt
from .utils import request_id, temp_session_id
import pickle
from server_app.models import Users, GuestDatatable


# print(app.config.SQLALCHEMY_DATABASE_URI)
# NatureSines SQLaclmy app
# https://flask.palletsprojects.com/en/2.0.x/debugging/
@bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@bp.route("/UploadAudio",  methods=['GET', 'POST'])
def uploadAudio():
    # CORS issue solved
    if request.method == "POST":
        print("Request is POST!")
        audioData = request.data
        # take the raw binary pickle? 
        # creating a binary blob 
        # insert a unique column types large binary object or Blob
        # SERALIAZAIION 
        pickled_data = pickle.dumps(audioData)

        # blobs in postgreSQL b'\' miners hat to enter cave
        insertData = GuestDatatable(username='Guest', password='Guest', audio=pickled_data)
        
        try: 
            db.session.add(insertData)
            db.session.commit()
        except Exception as e:
            print("An exception occurred: ", e) 
            return jsonify("Audio binary didnt save into database failed", 500)
        # dump binary?

    print("Hello Audio Upload")
    return jsonify("success", 200)
