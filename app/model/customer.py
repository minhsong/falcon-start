# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String, Integer, LargeBinary,DateTime
from sqlalchemy.dialects.postgresql import JSONB

from app.model import Base
from app.utils import alchemy


class Customer(Base):
    user_id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(320), unique=True, nullable=False)
    dob = Column(DateTime(), nullable=True)

    def __repr__(self):
        return "<Customer(name='%s', email='%s', dob='%s)>" % \
            (self.name, self.email, self.dob)

    @classmethod
    def get_id(cls):
        return Customer.user_id

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(Customer).filter(Customer.email == email).one()

    FIELDS = {
        'username': str,
        'email': str,
        'info': alchemy.passby,
        'token': str
    }

    FIELDS.update(Base.FIELDS)
