from app.main import main
from flask import render_template, current_app

@main.route("/")
@main.route("/index")
def index():
    print()
    print(current_app.config["ENV"])
    print()
    return render_template('base.html')