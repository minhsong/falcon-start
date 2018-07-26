# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String, Integer, LargeBinary,DateTime
from sqlalchemy.dialects.postgresql import JSONB

from app.model import Base
from app.utils import alchemy


class Customer(Base):
    _id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(320), unique=True, nullable=False)
    dob = Column(DateTime(), nullable=True)

    def __repr__(self):
        return "<Customer(_id='%s',name='%s', email='%s', dob='%s)>" % \
            (self._id, self.name, self.email, self.dob)

    @classmethod
    def get_id(cls):
        return Customer._id

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(Customer).filter(Customer.email == email).one()

    FIELDS = {
        '_id':int,
        'name': str,
        'email': str,
        'dob': alchemy.datetime_to_timestamp
    }

    FIELDS.update(Base.FIELDS)
