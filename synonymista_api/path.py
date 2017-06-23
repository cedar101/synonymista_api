# -*- encoding: utf-8 -*-
from .app import App
from . import model     # import Word, WordSimilarity
from . import collection    # import WordCollection, WordSimilarityCollection


@App.path(model=model.Word, path='/words/{id}')
def get_word(id=0):
    return model.Word[id]


@App.path(model=collection.WordCollection, path='/words')
def get_words(page=1, order=0, extra_parameters=None):
    return collection.WordCollection(page, order, extra_parameters)


@App.path(model=model.WordSimilarity, path='/word-similarities/{id}')
def get_word_similarity(id=0):
    return model.WordSimilarity[id]


@App.path(model=collection.WordSimilarityCollection, path='/word-similarities')
def get_word_similarity_collection(page=1, order=0, extra_parameters=None):
    return collection.WordSimilarityCollection(page, order, extra_parameters)
