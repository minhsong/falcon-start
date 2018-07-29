import falcon
import datetime
from sqlalchemy import or_,DateTime, func
from sqlalchemy.orm.exc import NoResultFound
from app.api.base import BaseResource
from app.model import Customer
from app.utils.authHooks import auth_required
from app.errors import InvalidParameterError

from app import log
LOG = log.get_logger()

class CustomerCreateAPI(BaseResource):
    @falcon.before(auth_required)
    def on_post(self,req,res):
        session = req.context['session']
        rawData = req.context['data']
        format_str = '%d/%m/%Y' # The format
        if rawData['email'] and rawData['name']:
            isExistedEmailCus = session.query(Customer).filter(Customer.email==rawData['email']).first()
            LOG.debug(isExistedEmailCus)
            if isExistedEmailCus:
                raise InvalidParameterError('Email is used in system!')
            else:
                cus = Customer()
                cus.email = rawData['email']
                cus.name = rawData['name']
                cus.dob = datetime.datetime.strptime(rawData['dob'], format_str) #dob format dd/mm/yyyy
                session.add(cus)
        else:
            raise InvalidParameterError('email and name are required!')
    

class CustomerAPI(BaseResource):
    
    @falcon.before(auth_required)
    def on_put(self,req,res,_id):
        session = req.context['session']
        rawData = req.context['data']
        format_str = '%d/%m/%Y' # The format
        if _id:
            if rawData['email'] and rawData['name']:
                cus = session.query(Customer).get(_id)
                isExistedEmailCus = session.query(Customer).filter(Customer.email==rawData['email']).first()
                if isExistedEmailCus and isExistedEmailCus._id!=cus._id:
                    raise InvalidParameterError('Email is used, please chose other email')
                if cus:
                    cus.email = rawData['email']
                    cus.name = rawData['name']
                    cus.dob = datetime.datetime.strptime(rawData['dob'], format_str)
                    cus.modified = func.now()
                    session.commit()
                    self.on_success(res,cus.to_dict())
                else:
                    raise InvalidParameterError('Customer not found!')
        else:
            raise InvalidParameterError('_id is required')
        
    
    @falcon.before(auth_required)
    def on_get(self,req,res,_id):
        session = req.context['session']
        if _id:
            cus = session.query(Customer).get(_id)
            self.on_success(res,cus.to_dict())
        else:
            raise InvalidParameterError('_id is required')

    def on_delete(self,req,res,_id):
        if _id:
            session = req.context['session']
            session.query(Customer).filter(Customer._id==_id).delete()
            self.on_success(res,None)
        else:
            raise InvalidParameterError('_id is required')

class CustomerList(BaseResource):
    @falcon.before(auth_required)
    def on_get(self,req,res):
        session = req.context['session']
        result = session.query(Customer).all()
        result = [ item.to_dict() for item in result]
        self.on_success(res,result)

    @falcon.before(auth_required)
    def on_post(self,req,res):
        session = req.context['session']
        rawData = req.context['data']
        page = 1
        itemPerPage = 10
        searchString = rawData['str'].strip().lower()
        if rawData['page']:
            page = int(rawData['page'])
            if page <1:
                page =1
        
        if rawData['itemPerPage']:
            itemPerPage = int(rawData['itemPerPage'])
            if itemPerPage <1:
                itemPerPage =10
        try:
            result = session.query(Customer).filter(or_(func.lower(Customer.name) \
                .contains(searchString),func.lower(Customer.email).contains(searchString),)) \
                .order_by(Customer.email.desc()) \
                .limit(itemPerPage).offset((page - 1) * itemPerPage).all()
            result = [ item.to_dict() for item in result]
            result = {
                "list":result,
                "page":page,
                "itemPerPage":itemPerPage,
                "total":session.query(Customer).count()
            }
            self.on_success(res,result)
        except NoResultFound:
            self.on_success(res,None)
        