import falcon
from app.api.base import BaseResource
class User(BaseResource):
    def on_post(self,req,res):
        self.on_success(res,None)
    def on_get(self,req,res):
        self.on_success(res,None)