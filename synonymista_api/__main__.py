# -*- encoding: utf-8 -*-
import morepath
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication

from .app import App
from .model import db


DB_TYPE = 'mysql'
DB_PORT = 3306
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'digital'
DB_NAME = 'synonymista'
DB_CHARSET = 'utf8'


def setup_db(app=None):
    db.bind(DB_TYPE, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
            # create_db=True)
    db.generate_mapping(create_tables=True)


def run():
    setup_db()
    morepath.autoscan()
    App.commit()
    run_simple('0.0.0.0', 5000,
               DebuggedApplication(App(), evalex=True),
               use_reloader=True)
    # morepath.run(App())


if __name__ == '__main__':
    run()
