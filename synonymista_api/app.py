# -*- encoding: utf-8 -*-
import morepath
from more.pony import PonyApp

class App(PonyApp): # (morepath.App):
    pass

@App.tween_factory()
def make_tween(app, handler):
    def add_cors(request):
        response = handler(request)
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        return response
    return add_cors
