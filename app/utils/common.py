import shortuuid

import jwt
import bcrypt
from app.config import UUID_LEN, UUID_ALPHABET,JWT_SECRET_KEY

def uuid():
    return shortuuid.ShortUUID(alphabet=UUID_ALPHABET).random(UUID_LEN)


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(password, hashed):
    return bcrypt.hashpw(password.encode('utf-8'), hashed) == hashed

def encode_jwt(payload):
    try:
        data = jwt.encode(payload, JWT_SECRET_KEY,algorithm='HS256')
        return data
    except:
        return None

def decode_jwt(token):
    try:
        data = jwt.decode(token, JWT_SECRET_KEY,algorithm='HS256')
        return data
    except:
        return None