'''
This file is our entry point for our flask app to run
'''

from app import create_app

# Call and store the app from app/__init__.py
app = create_app()

if(__name__) == "__main__":
    app.run()