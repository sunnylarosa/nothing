'''This file contain all the routes for auth/ module'''

from app.auth import auth

@auth.route("/login")
def login():
    return "Login Page"