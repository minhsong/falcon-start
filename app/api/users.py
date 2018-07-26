import falcon
from app.api.base import BaseResource
from app.model import User
from app.errors import AppError, InvalidParameterError, UserNotExistsError, PasswordNotMatch
from app.utils.common import uuid,hash_password

FIELDS = {
    'email': {
        'type': 'string',
        'regex': '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}',
        'required': True,
        'maxlength': 320
    },
    'password': {
        'type': 'string',
        'regex': '[0-9a-zA-Z]\w{3,14}',
        'required': True,
        'minlength': 8,
        'maxlength': 64
    }
}

class UserController(BaseResource):
    def on_post(self,req,res):
        session = req.context['session']
        rawData = req.context['data']
        if rawData['email'] and rawData['password'] :
            newUser = User()
            newUser.email=rawData['email']
            newUser.password = hash_password(rawData['password']).decode('utf-8')
            newUser.sid = uuid()
            session.add(newUser)
            res.body = newUser
        else:
            raise InvalidParameterError(req.context['data'])
        self.on_success(res,{"email":newUser.email})
    def on_get(self,req,res):
        self.on_success(res,None)