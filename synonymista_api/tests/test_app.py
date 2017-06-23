import morepath
import synonymista_api

from webtest import TestApp as Client


def test_root():
    morepath.scan(synonymista_api)
    morepath.commit(synonymista_api.App)

    client = Client(synonymista_api.App())
    root = client.get('/')

    assert root.status_code == 200
    assert len(root.json['greetings']) == 2
