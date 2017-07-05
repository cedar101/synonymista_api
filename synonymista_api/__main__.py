# -*- encoding: utf-8 -*-
import yaml
import morepath
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication

from .app import App
from .model import db


# DB_TYPE = 'mysql'
# DB_PORT = 3306
# DB_HOST = 'localhost'
# DB_USER = 'root'
# DB_PASSWORD = 'digital'
# DB_NAME = 'synonymista'
# DB_CHARSET = 'utf8'


def setup_db(app=None):
    provider = app.settings.database.provider
    args = app.settings.database.args
    kwargs = app.settings.database.kwargs
    db.bind(provider, *args, **kwargs)
    # db.bind(DB_TYPE, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
    #         # create_db=True)
    db.generate_mapping(create_tables=True)


def run():
    morepath.autoscan()

    with open('settings/default.yaml') as defaults:
        defaults_dict = yaml.load(defaults)

    App.init_settings(defaults_dict)
    App.commit()
    app = App()
    setup_db(app)

    run_simple(app.settings.run.host,
               app.settings.run.port,
               DebuggedApplication(app, evalex=True),
               use_reloader=True)
    # morepath.run(App())


if __name__ == '__main__':
    run()
