'''
This __init__.py file used to bring in our application together
and declare our app variable. Also tells Python Interpreter that
this (/app) is a package.
'''
from flask import Flask
import config

def create_app(config_filename=config):
    app = Flask(__name__)

    if app.config["ENV"] == "production":
        app.config.from_object(config_filename.ProductionConfig)
        
    elif app.config["ENV"] == "development":
        app.config.from_object(config_filename.DevelopmentConfig)

    # Import "main" as the "main_bp" then register the blueprint
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    # Import "auth" as the "auth_bp" then register the blueprint
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app



# from app import routes