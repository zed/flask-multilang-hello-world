#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, g, redirect, request, render_template, url_for
from flask.ext.babel import Babel, gettext # $ pip install flask-babel

# available languages
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
}

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())

@app.before_request
def before_request():
    g.locale = get_locale()

@app.route('/')
def index():
    return render_template('index.html', who=gettext('world'))

@app.route('/redirect')
def redirected():
    if g.locale == 'ru':
        return redirect(url_for('index'))
    return 'no redirect'

if __name__=="__main__":
    app.run(debug=True, port=28015, host='localhost')
