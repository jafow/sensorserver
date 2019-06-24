import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def init_db(app):
    """ run schema.sql; creates a climate table """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql') as schema:
            db.executescript(schema.read().decode('utf8'))
        db.commit()


def get_db():
    """ get a connection to the db """
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """ teardown the db connection """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
