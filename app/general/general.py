'''
This file is about all the views or routes of general package.
General package contains the process and the files of common 
page such as home/index, login, logout, sign up, etc.
'''
from flask import Blueprint, render_template

General = Blueprint("General", __name__, template_folder="templates", url_prefix="/")

# @General.route("/")
# def index():
#     # return "<h1>Hello</h1>"
#     return render_template("starter.html")

@General.route("/about")
def about():
    return "<h1>This is General about page</h1>"