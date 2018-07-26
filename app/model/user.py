# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String, Integer, LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from app.model import Base
from app.utils import alchemy


class User(Base):
    user_id = Column(Integer, primary_key=True)
    email = Column(String(320), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    token = Column(String(500), nullable=True)

    # intentionally assigned for user related service such as resetting password: kind of internal user secret key
    sid = Column(String(250), nullable=False)

    def __repr__(self):
        return "<User(email='%s',password=%s')>" % \
            (self.email,self.password)

    @classmethod
    def get_id(cls):
        return User.user_id

    @classmethod
    def find_by_email_and_password(cls, session, email,password):
        return session.query(User).filter(User.email == email).filter(User.password==password).one()

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(User).filter(User.email == email).one()
    FIELDS = {
        'email': str,
        'token': str
    }

    FIELDS.update(Base.FIELDS)
