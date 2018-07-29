# -*- coding: utf-8 -*-

import falcon

from app.api.base import BaseResource
from app.api.auth import Auth
from app.api.users import UserController
from app.errors import AppError
from app.middleware import JSONTranslator, DatabaseSessionManager, AuthHandler
from app.database import db_session, init_session
from app.api.customer import CustomerCreateAPI,CustomerAPI,CustomerList

init_session()
middleware = [AuthHandler(db_session), JSONTranslator(), DatabaseSessionManager(db_session)]
application = falcon.API(middleware=middleware)
application.add_route('/', BaseResource())
application.add_route('/auth/login', Auth())
application.add_route('/user/create', UserController())

application.add_route('/customer', CustomerCreateAPI())
application.add_route('/customer/{_id}', CustomerAPI())
application.add_route('/customers', CustomerList())
application.add_error_handler(AppError, AppError.handle)
