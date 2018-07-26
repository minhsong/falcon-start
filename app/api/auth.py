import falcon

from sqlalchemy.orm.exc import NoResultFound
from app.config import JWT_SECRET_KEY
from app import log
from app.api.base import BaseResource
from app.model import User
from app.errors import AppError, InvalidParameterError, UserNotExistsError, PasswordNotMatch
from app.utils.common import uuid,hash_password,verify_password,encode_jwt

LOG = log.get_logger()

class Auth(BaseResource):
    def on_post(self,req,res):
        session = req.context['session']
        loginData = req.context['data']
        LOG.debug('login user: %s',loginData)
        email = loginData['email']
        password = loginData['password']
        
        try:
            user = User.find_by_email(session,email)
            if user and verify_password(password, user.password.encode('utf-8')):
                payload = {
                    'user_id': user.user_id,
                    'email': user.email,
                }
                jwt_token = encode_jwt(payload)
                user.token = jwt_token
                session.commit()
                self.on_success(res, user.to_dict())
            else:
                raise PasswordNotMatch()
        except NoResultFound:
            self.on_success(res,None)
