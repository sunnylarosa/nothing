from app.main import main
from flask import render_template, current_app
import os

@main.route("/")
@main.route("/index")
def index():
    print()
    print(f"\nFlask ENV is set to: {current_app.config['ENV']}")
    print(f"DB_NAME = {current_app.config['DB_NAME']}\n")
    print()
    return render_template('base.html')