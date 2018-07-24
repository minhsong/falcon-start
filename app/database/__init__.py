# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

def get_engine(uri):
    options = {
        'pool_recycle': 3600,
        'pool_size': 10,
        'pool_timeout': 30,
        'max_overflow': 30,
        'echo': True,
        'execution_options': {
            'autocommit': True
        }
    }
    return create_engine(uri, **options)


db_session = scoped_session(sessionmaker())
db_string = "postgres://postgres:123@localhost/challenge"
engine = get_engine(db_string)


def init_session():
    db_session.configure(bind=engine)

    from app.model import Base
    Base.metadata.create_all(engine)
