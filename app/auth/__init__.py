'''
This file contain the initialization of module = auth/.
Blueprint name = auth
Static folder name = static
Templates folder name = templates

Generate URL
------------
- Static
    Endpoint name = auth.static
    Static URL = /auth/static
    Generate URL =
        url_for('auth.static', filename='style.css')

- Templates
    *Assume we have an index.html file inside templates/auth*
    Endpoint name = auth.index
    Templates URL or when using render_template() =
        render_template('auth/index.html')
    Generate URL = 
        url_for(auth.index)
    
'''

from flask import Blueprint

# Create the bluprint for auth/ module
auth = Blueprint('auth', __name__, url_prefix="/auth", static_folder="static", template_folder="templates")

# Import the views / routes
from app.auth import routes