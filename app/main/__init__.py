'''
This file contain the initilization of module main/
main/ module is about all the common views or routes like index.html, etc.

This module was created without url prefix
'''

from flask import Blueprint

# Create the bluprint for auth/ module
main = Blueprint('main', __name__)

# Import the views or routes
from app.main import routes