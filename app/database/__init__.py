# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import DB_CONNECTING_STRING

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
engine = get_engine(DB_CONNECTING_STRING)


def init_session():
    db_session.configure(bind=engine)

    from app.model import Base
    Base.metadata.create_all(engine)
