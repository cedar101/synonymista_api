# -*- encoding: utf-8 -*-
import webob.exc
from pony.orm import db_session, desc

from .model import db, Word, WordSimilarity

class Collection(object):
    Model = db.Entity

    def __init__(self, page_num=1, page_size=10, sort=None,
                 extra_parameters=None):
        self.page_num = page_num
        self.page_size = page_size
        self.start = (page_num - 1) * page_size
        self.end = page_num * page_size
        self.sort = sort
        self.extra_parameters = extra_parameters
        self.filter_func = None

    @db_session
    def query(self):
        select = self.__class__.Model.select
        selected = (select()
                    if self.filter_func is None
                    else select(self.filter_func))
        if self.sort:
            attr_str, sep, order = self.sort.partition('|')
            attr = getattr(self.__class__.Model, attr_str)
            if order == 'desc':
                attr = desc(attr)
            selected = selected.order_by(attr)
        try:
            return selected.page(self.page_num, self.page_size)
        except TypeError:
            raise webob.exc.HTTPRequestRangeNotSatisfiable()

    @db_session
    def add(self, **kwargs):
        entity = self.__class__.Model(**kwargs)
        return entity

    @db_session
    def count(self):
        return self.__class__.Model.select().count()

    def last_page(self):
        return self.count() // self.page_size + 1

    def previous(self):
        return self.__class__(max(1, self.page_num-1),
                              self.page_size, self.sort, self.extra_parameters)

    def next(self):
        return self.__class__(min(self.page_num+1, self.count()),
                              self.page_size, self.sort, self.extra_parameters)


class WordCollection(Collection):
    Model = Word

    def __init__(self, page_num=1, page_size=10, sort=None,
                 extra_parameters=None):
        super().__init__(page_num, page_size, sort, extra_parameters)

        try:
            query = extra_parameters['filter']
        except (TypeError, KeyError):
            self.filter_func = None
        else:
            self.filter_func = {
                'contains': lambda w: query in w.value,
                'startswith': lambda w: w.value.startswith(query),
                'endswith': lambda w: w.value.endswith(query),
                'eq': lambda w: w.value == query
            }[extra_parameters.get('cond', 'contains')]


class WordSimilarityCollection(Collection):
    Model = WordSimilarity

    def __init__(self, page_num=1, page_size=10, sort=None,
                 extra_parameters=None):
        super().__init__(page_num, page_size, sort, extra_parameters)

        try:
            query = extra_parameters['filter']
        except (TypeError, KeyError):
            self.filter_func = None
        else:
            self.filter_func = {
                'contains': lambda ws: (query in ws.subject_word.value or
                                        query in ws.similar_word.value),
                'startswith': lambda ws: (ws.subject_word.value.startswith(query) or
                                          ws.similar_word.value.startswith(query)),
                'endswith': lambda ws: (ws.subject_word.value.endswith(query) or
                                        ws.similar_word.value.endswith(query)),
                'eq': lambda ws: (ws.subject_word.value == query or
                                  ws.similar_word.value == query)
            }[extra_parameters.get('cond', 'contains')]
