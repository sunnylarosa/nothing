'''
This __init__.py file used to bring in our application together
and declare our app variable. Also tells Python Interpreter that
this (/app) is a package.
'''
from flask import Flask

def create_app(config_filename=None):
    app = Flask(__name__)

    # Import then register 'main' blueprint
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    # Import then register 'auth' blueprint
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app



# from app import routes