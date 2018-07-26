# -*- coding: utf-8 -*-

import sqlalchemy.orm.scoping as scoping
from app import log
from app.errors import UnauthorizedError
from app.utils.common import decode_jwt
from app.model import User

LOG = log.get_logger()


class AuthHandler(object):
    def __init__(self, db_session):
        self._session_factory = db_session
        self._scoped = isinstance(db_session, scoping.ScopedSession)
    def process_request(self, req, res):
        authToken = req.get_header('Authorization')
        if authToken is not None:
            auth_user = decode_jwt(authToken)
            LOG.debug("auth_user: %s", auth_user)
            if auth_user is None:
                raise UnauthorizedError('Invalid authentication token')
            else:
                session = self._session_factory
                db_user = session.query(User).get(auth_user['user_id'])
                LOG.debug("db_user: %s", db_user)
                if db_user:
                    req.context['auth_user'] = auth_user
                else:
                    req.context['auth_user'] = None
        else:
            req.context['auth_user'] = None
