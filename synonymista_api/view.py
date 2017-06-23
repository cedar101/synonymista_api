# -*- encoding: utf-8 -*-
from datetime import datetime
import dateutil.parser
import morepath

from .app import App
from . import model
from . import collection

def datetime_decode(s):
    return dateutil.parser.parse(s)

def datetime_encode(d):
    return d.isoformat()

@App.converter(type=datetime)
def datetime_converter():
    return morepath.Converter(datetime_decode, datetime_encode)


def to_dict(entity, request=None, link=True):
    result = entity.to_dict(with_collections=True, related_objects=True)
    if link:
        result['link'] = request.link(entity)
    return result


@App.json(model=model.Word)
def view_word(self, request):
    result = to_dict(self, request)
    similar_to = result['similar_to']
    similar_from = result['similar_from']
    result['similar_to'] = [request.link(ws) for ws in similar_to]
    result['similar_from'] = [request.link(ws) for ws in similar_from]
    return result


@App.json(model=collection.WordCollection)
def view_word_collection(self, request):
    return {
        'words': [request.view(doc) for doc in self.query()],
        'previous': request.link(self.previous(), default=None),
        'next': request.link(self.next(), default=None),
        'add': request.link(self, 'add'),
    }


@App.json(model=model.WordSimilarity, converter=datetime_converter)
def view_word_similarity(self, request):
    result = to_dict(self, request)
    result['update_date'] = datetime_encode(result['update_date'])
    result['subject_word'] = request.link(result['subject_word'])
    result['similar_word'] = request.link(result['similar_word'])
    return result


@App.json(model=collection.WordSimilarityCollection)
def view_word_similarity_collection(self, request):
    return {
        'word_similarities': [request.view(doc) for doc in self.query()],
        'previous': request.link(self.previous(), default=None),
        'next': request.link(self.next(), default=None),
        'add': request.link(self, 'add'),
    }
