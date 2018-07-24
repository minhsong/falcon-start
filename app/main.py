# -*- coding: utf-8 -*-

import falcon

from app.api.base import BaseResource
from app.errors import AppError
from app.middleware import JSONTranslator, DatabaseSessionManager
from app.database import db_session, init_session

init_session()
middleware = [JSONTranslator(), DatabaseSessionManager(db_session)]
application = falcon.API(middleware=middleware)
application.add_route('/', BaseResource())
application.add_error_handler(AppError, AppError.handle)