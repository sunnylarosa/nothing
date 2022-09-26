'''
This run.py file used to declare our app variable bring
in our application together

Import Package / Modules:
----------------------------
Under this comment is the part where we import all project modules 
with command:
        from <package_name>.<filename> import <object>

Register:
------------
Under this comment is the part where we register all the Blueprints
into our web application. In other words, we extend the application 
with it's contents (Blueprint).
'''

# Import Package / Modules
from flask import Flask, render_template
from general.general import General

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(General)

# Run the application
if (__name__) == "__main__":
    app.run()