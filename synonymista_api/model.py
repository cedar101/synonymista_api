# -*- encoding: utf-8 -*-
from datetime import datetime

from pony.orm import Database, Set, Optional, Required, db_session, select, delete, sql_debug
import click

db = Database()

sql_debug(True)

# @app.before_first_request
# def generate_mapping():
#     db.generate_mapping()


class GetCreateMixin(object):
    @classmethod
    def get_or_create(cls, **params):
        o = cls.get(**params)
        return cls(**params) if o is None else o


class UpdateMixin(object):
    def update(self, payload):
        self.set(**payload)


class Word(db.Entity, GetCreateMixin):
    _table_ = 'word'
    value = Required(str, unique=True)
    similar_to = Set('WordSimilarity', reverse='subject_word')
    similar_from = Set('WordSimilarity', reverse='similar_word')
    create_at = Required(datetime, default=datetime.now())
    update_at = Required(datetime, default=datetime.now())


class WordSimilarity(db.Entity, GetCreateMixin):
    _table_ = 'word_similarity'
    value = Required(float)
    subject_word = Required(Word, reverse='similar_to')
    similar_word = Required(Word, reverse='similar_from')
    create_at = Required(datetime, default=datetime.now())
    update_at = Required(datetime, default=datetime.now())
    confirmed = Optional(bool)


# @app.cli.command()
def initdb():
    """Initialize the database."""
    print('Initing the db....')
    if click.confirm('Do you want to drop the table?'):
        db.drop_table('word', if_exists=True, with_all_data=True)
        db.drop_table('word_similarity', if_exists=True, with_all_data=True)
    db.generate_mapping(create_tables=True)
    click.echo('Inited the db.')


@db_session
def get_selected_words(word_value):
    word_similarities = select((wordsim.similar_word.value, wordsim.value)
                               for word in Word
                               for wordsim in word.similar_to
                               if word.value == word_value)
    return word_similarities[:] if word_similarities else []


@db_session
def save_selected_words(word_value, selected_data):
    delete(wsim for w in Word for wsim in w.similar_to if w.value == word_value)
    word = Word.get_or_create(value=word_value)
    word.similar_to = [WordSimilarity.get_or_create(
                                        value=sim,
                                        similar_word=Word.get_or_create(value=w),
                                        subject_word=word
                                      )
                       for w, sim in selected_data]
