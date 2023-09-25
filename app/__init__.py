from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watamu.db'

    #third party packages
    db = SQLAlchemy(app)
    #add routes
    from app import routes
    app.register_blueprint(routes.main)


    return app