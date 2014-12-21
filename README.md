Show response in user language.

Use HTTP Accept-Languages header (most browsers allow to configure
it. The default value comes from OS).

Based on the tutorial:
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-i18n-and-l10n

Installation:

    $ pip install flask flask-babel

To create messages.pot:

    $ pybabel extract -F babel.cfg -o messages.pot .

To add Russian translation to the app:

    $ pybabel init -i messages.pot -d translations -l ru

After the translation is done (messages.po is edited), publish changes:

    $ pybabel compile -d translations

TODO:
- set language in HTTP GET hl parameter/url path
- set language via cookies
- set language in session var
