from app import app
from flask import render_template, session, redirect, request

@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'sv'  # Set default language to Swedish here

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    # Pop the session variable to None to force an overwrite
    session.pop('language', None)
    # Set the session variable lang to whatever code was used in the URL
    session["language"] = lang_code
    # Refresh the page from which the set language request was made
    return redirect(request.referrer)
