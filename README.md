Show response in user language.

Use language specified in the url (in the path or as a `lang` query
parameter) or in HTTP `Accept-Languages` header (most browsers allow to
configure it. The default value comes from OS).

Based on the tutorial:
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-i18n-and-l10n

### To try it

Install:

    $ pip install flask flask-babel

Create `messages.pot`:

    $ pybabel extract -F babel.cfg -o messages.pot .

Update `.po` files if necessary (if any of `.py` or templates files have been changed):

    $ pybabel update -i messages.pot -d translations

After the translation is done (messages.po is edited), publish changes:

    $ pybabel compile -d translations

To start the debug applicaiton:

    $ python multilang-app.py

and visit http://localhost:28015/

To test the redirection, visit http://localhost:28015/ru/redirect

### How to add a new translation

To add a new language (to create corresponding `.po` files) e.g., Russian, run:

    $ pybabel init -i messages.pot -d translations -l ru

edit `.po` file to provide the translation then build it (to get `.mo` files):

    $ pybabel compile -d translations

and update available `LANGUAGES` dict in `multilang-app.py`.

### How to deploy on heroku

    $ heroku login
    $ heroku create
    $ git push heroku master
    $ heroku ps:scale web=1  # make sure it's running
    $ heroku open  # open browser

### TODO

- set language via cookies
- set language in session var
