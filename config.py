'''
This file contains the configuration class for this flask application.
This key,value pairs will later be the configuration for app (app.config["KEY"]).

About SESSION_COOKIE:
    Session cookie means that it will only send cookies back and forth
    if there is a secure HTTPS connection.
    Since the development and testing not going to be running over HTTPS, 
    change it to False.
'''
import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')

    # DATABASE
    DB_NAME = "production-db"
    DB_DRIVER = "ODBC Driver 11 for SQL Server"

    # DIRECTORY PATH
    DIR_UPLOAD = os.getenv('DIR_UPLOAD_PROD')
    DIR_DOWNLOAD = os.getenv('DIR_DOWNLOAD_PROD')

    # MAIL for email
    MAIL_SERVER = "smtprelay.kalbe.co.id"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False

    # ROOT URL PREFIX
    ROOT_PREFIX = "/SASKI" 

    # SESSION COOKIES
    SESSION_COOKIE_SECURE = True
    
class ProductionConfig(Config):
    '''
    We just going to leave this inherit everything from the base class,
    leave them be.
    '''
    pass

class DevelopmentConfig(Config):
    # DATABASE
    DB_NAME = "development-db"
    DB_DRIVER = "ODBC Driver 17 for SQL Server"

    # DIRECTORY PATH
    DIR_UPLOAD = os.getenv('DIR_UPLOAD_DEV')
    DIR_DOWNLOAD = os.getenv('DIR_DOWNLOAD_DEV')

    # MAIL for email
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "sunnylarosa121@gmail.com"
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    # SESSION COOKIES
    SESSION_COOKIE_SECURE = False