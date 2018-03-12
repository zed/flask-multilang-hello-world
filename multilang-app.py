#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import (abort, Flask, g, redirect, request,
                   render_template, send_from_directory, url_for)
from flask_babel import Babel, gettext as _  # $ pip install flask-babel

# available languages
LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
}

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return g.lang


@app.before_request
def before_request():
    if request.view_args and 'lang' in request.view_args:
        g.lang = request.view_args['lang']
        request.view_args.pop('lang')
    elif request.args.get('lang'):
        g.lang = request.args.get('lang')
    else:
        g.lang = request.accept_languages.best_match(LANGUAGES.keys()) or 'en'
    if g.lang not in LANGUAGES:
        abort(404)


@app.route('/<lang>')
def lang():
    return render_template('index.html', who=_('world'))


@app.route('/')
def index():
    return redirect(url_for('lang', lang=g.lang))


@app.route('/<lang>/redirect')
def redirected():
    if g.lang == 'ru':
        return redirect(url_for('index', lang=g.lang))
    return _('no redirect')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               _('favicon.ico'), mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True, port=28015, host='localhost')
