from flask import Flask, session
from flask_babel import Babel

#This will set the language variable in session for the Babel app
def get_locale():
    if 'language' in session:
        return session['language']
    else:
        session['language']='sv'
    return session['language']

#Create the flask app
app = Flask(__name__)
#We are going to use the session to manage language then we need to set a secret key
app.secret_key='a secret key'

#Hook Babel into your app
babel = Babel(app)
#Initiate the Babel app passing through the locale you want to start with
babel.init_app(app, locale_selector=get_locale)


#Import your routes (you need to configure these in routes.py)
from app import routes