
from flask import Flask
from flask_migrate import Migrate
from datetime import timedelta
from flask_jwt_extended import JWTManager
from extension import db 



app = Flask(__name__)

# Configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- JWT config ---
app.config["JWT_SECRET_KEY"] = "change-me"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

jwt = JWTManager(app)

import routes
import model 
import Function

db.init_app(app) 

migrate = Migrate(app, db) 



if __name__ == '__main__':
    app.run()