# -*- encoding: utf-8 -*-
from datetime import datetime
import dateutil.parser
import morepath
from pony.orm import db_session

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
    result['create_at'] = datetime_encode(result['create_at'])
    result['update_at'] = datetime_encode(result['update_at'])
    return result


@App.json(model=model.WordSimilarity, converter=datetime_converter)
def view_word_similarity(self, request):
    result = to_dict(self, request)
    result['subject_word'] = request.view(result['subject_word'])
    result['similar_word'] = request.view(result['similar_word'])
    result['create_at'] = datetime_encode(result['create_at'])
    result['update_at'] = datetime_encode(result['update_at'])
    return result


@App.json(model=model.WordSimilarity, converter=datetime_converter,
          request_method='DELETE')
def delete_word_similarity(self, request):
    with db_session:
        self.delete()
    return 'deleted'


@App.json(model=collection.Collection)
def collection_default(self, request):
    return {
        'data': [request.view(doc) for doc in self.query()],
        'links': {
            "pagination": {
                'prev_page_url': request.link(self.previous(), default=None),
                'next_page_url': request.link(self.next(), default=None),
                'total': self.count(),arom
                'current_page': self.page_num,
                'per_page': self.page_size,
                'last_page': self.last_page(),
                'from': self.start,
                'to': self.end
            }
        }
    }


@App.json(model=collection.WordCollection)
def view_word_collection(self, request):
    return collection_default(self, request)


@App.json(model=collection.WordSimilarityCollection)
def view_word_similarity_collection(self, request):
    return collection_default(self, request)
