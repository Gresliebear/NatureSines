
from flask import Flask, current_app
import os
import logging
from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from server_app.config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()

def create_app(config_class=Config):
    root_path = os.getcwd()
    app = Flask(__name__) 
    app.config.from_object(Config) # reference to config.py
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, supports_credentials=True )

    with app.app_context():
        from .main import bp as main_bp
        app.register_blueprint(main_bp)
        
        return app