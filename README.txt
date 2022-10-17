Example from https://github.com/miguelgrinberg/microblog:
---------------------------------------------------------
microblog
|-- app/
|   |-- api/
|   |   |-- __init__.py
|   |   |-- auth.py
|   |   |-- errors.py
|   |   |-- tokens.py
|   |   |-- users.py (routes)
|   |   
|   |-- auth/
|   |   |-- __init__.py
|   |   |-- email.py
|   |   |-- forms.py
|   |   |-- routes.py
|   |
|   |-- errors/
|   |   |-- __init__.py
|   |   |-- handlers.py
|   |   
|   |-- main/
|   |   |-- __init__.py
|   |   |-- forms.py
|   |   |-- routes.py
|   |
|   |-- static/
|   |   |-- loading.gif
|   |   
|   |-- templates/
|   |   |-- auth/
|   |   |   |-- login.html
|   |   |   |-- register.html
|   |   |   |-- reset_password.html
|   |   |   |-- reset_password_request.html
|   |   |   
|   |   |-- email/
|   |   |   |-- export_posts.html
|   |   |   |-- export_posts.txt
|   |   |   |-- reset_password.html
|   |   |   |-- reset_password.txt
|   |   |   
|   |   |-- errors/
|   |   |   |-- 404.html
|   |   |   |-- 500.html
|   |   | 
|   |   |-- _post.html
|   |   |-- base.html
|   |   |-- edit_profile.html
|   |   |-- index.html
|   |   |-- messages.html
|   |   |-- search.html
|   |   |-- send_message.html
|   |   |-- user.html
|   |   |-- user_popup.html
|   |   
|   |-- translations/es/LC_MESSAGES
|   |-- __init__.py
|   |-- cli.py
|   |-- email.py
|   |-- models.py
|   |-- search.py
|   |-- tasks.py
|   |-- translate.py
|   
|-- deployment/
|   |-- nginx/
|   |-- supervisor/
|  
|-- migrations/
|   |-- versions/
|   |-- README
|   |-- alembic.ini
|   |-- env.py
|   |-- script.py.mako
|
|-- .flaskenv
|-- .gitattributes
|-- .gitignore
|-- Dockerfile
|-- LICENSE
|-- Procfile
|-- README.md
|-- Vagrantfile
|-- babel.cfg
|-- boot.sh
|-- config.py
|-- microblog.py (run file)
|-- requirements.txt
|-- tests.py



nothing
|-- app/
|   |-- auth/
|   |   |-- static/
|   |   |   |-- script.js
|   |   |   
|   |   |-- __init__.py
|   |   |-- routes.py
|   |
|   |-- main/
|   |   |-- __init__.py
|   |   |-- routes.py
|   |   
|   |-- static/
|   |   |-- dist/
|   |   |-- plugins/
|   |   |-- public/
|   |   |   |-- img/
|   |   |   |   |-- kalbe.jpg
|   |   |   |   |-- kalbe2.jpg
|   |
|   |-- templates/
|   |   |-- auth/
|   |   |   |-- login.html
|   |   |   |-- register.html
|   |   |
|   |   |-- main/
|   |   |   |-- welcome.html
|   |   |   
|   |   |-- base.html
|   |   |-- index.html
|   
|-- venv/  
|-- .gitignore
|-- README.txt
|-- saski.py (run file)































