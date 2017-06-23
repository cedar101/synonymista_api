# -*- encoding: utf-8 -*-
import webob.exc
from pony.orm import db_session, desc

from .model import db, Word, WordSimilarity

class Collection(object):
    Model = db.Entity

    def __init__(self, page=1, order=0, extra_parameters=None):
        self.page = (1 if page is None else page)
        self.order = order
        self.extra_parameters = extra_parameters
        self.filter_func = None

    @db_session
    def query(self):
        select = self.__class__.Model.select
        selected = (select()
                    if self.filter_func is None
                    else select(self.filter_func))
        if self.order != 0:
            selected = selected.order_by(self.order)
        try:
            return selected.page(self.page)
        except TypeError:
            raise webob.exc.HTTPRequestRangeNotSatisfiable()

    @db_session
    def add(self, **kwargs):
        entity = self.__class__.Model(**kwargs)
        return entity

    def previous(self):
        return self.__class__(max(1, self.page-1), self.order,
                              self.extra_parameters)

    @db_session
    def next(self):
        count = self.__class__.Model.select().count()
        return self.__class__(min(self.page+1, count), self.order,
                              self.extra_parameters)


class WordCollection(Collection):
    Model = Word

    def __init__(self, page=1, order=0, extra_parameters=None):
        super().__init__(page, order, extra_parameters)

        try:
            query = extra_parameters['q']
        except (TypeError, KeyError):
            self.filter_func = None
        else:
            try:
                cond = extra_parameters['cond']
            except KeyError:
                self.filter_func = lambda w: w.value == query
            else:
                if cond == 'contains':
                    self.filter_func = lambda w: query in w.value
                elif cond == 'startswith':
                    self.filter_func = lambda w: w.value.startswith(query)
                elif cond == 'endswith':
                    self.filter_func = lambda w: w.value.endswith(query)
                else:
                    self.filter_func = lambda w: w.value == query


class WordSimilarityCollection(Collection):
    Model = WordSimilarity
