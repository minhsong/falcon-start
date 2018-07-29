Falcon REST API with PostgreSQL and Json Web Token
===============================
Simple REST API using Falcon web framework.

Falcon is a high-performance Python framework for building cloud APIs, smart proxies, and app backends. More information can be found [here](https://github.com/falconry/falcon/).

Requirements
============
You may need a related dependency library for a PostgreSQL database and setup database.


Installation
============

Install all the python module dependencies in requirements.txt

```
  pip install -r requirements.txt
```
You have to change the PostreSQL connecting string in file app/config.py base in your server config
```
  DB_CONNECTING_STRING = "postgres://<postgres user>:<user password>@<your server>/<postgres database>"
```

Start server

```
  gunicorn -b 0.0.0.0:5000 app.main
```


Usage by Postman
=====
  User can import the "postman request example" file to [Postman](https://www.getpostman.com/) to test the api

Usage by call API
=====

Create with email and password

- Request
```shell
curl -XPOST http://localhost:5000/user \
    -H "Content-Type: application/json" \
    -d '{
            "email":"truongminhsong@gmail.com",
            "password":"123"
        }'
```

- Response
```json
{
    "meta": {
        "code": 200,
        "message": "OK"
    },
    "data": {
        "email":"truongminhsong@gmail.com"
    }
}
```
Log in with email and password

- Request
```shell
curl -XPOST http://localhost:5000/auth/login \
    -H "Content-Type: application/json" \
    -d '{
            "email":"truongminhsong@gmail.com",
            "password":"123"
        }'
```

- Response
```json
{
  "meta": {
    "code": 200,
    "message": "OK"
  },
  "data": {
    "username": "test1",
    "token": "gAAAAABV-TpG0Gk6LhU5437VmJwZwgkyDG9Jj-UMtRZ-EtnuDOkb5sc0LPLeHNBL4FLsIkTsi91rdMjDYVKRQ8OWJuHNsb5rKw==",
    "email": "test1@gmail.com",
    "created": 1442396742,
    "sid": "3595073989",
    "modified": 1442396742
  }
}
```

Create an user
- Request
    ```shell
    curl -XPOST http://localhost:5000/customer \
        -H "Content-Type: application/json" \
        -H "Authorization: gAAAAABV6Cxtz2qbcgOOzcjjyoBXBxJbjxwY2cSPdJB4gta07ZQXUU5NQ2BWAFIxSZlnlCl7wAwLe0RtBECUuV96RX9iiU63BP7wI1RQW-G3a1zilI3FHss=" \
        -d '{
                "email":"Vy22@gmail.com",
                "name":"Vy Nguyen",
                "dob":"24/03/1990"
            }'
    ```

- Response
    ```json
    {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": {
            "name": "Vy Nguyen",
            "created": 1532886545,
            "dob": 638236800,
            "modified": 1532886545,
            "_id": 13,
            "email": "Vy22@gmail.com"
        }
    }
    ```

Update an user
- Request
    ```shell
    curl -XPUT http://localhost:5000/customer/13 \
        -H "Content-Type: application/json" \
        -H "Authorization: gAAAAABV6Cxtz2qbcgOOzcjjyoBXBxJbjxwY2cSPdJB4gta07ZQXUU5NQ2BWAFIxSZlnlCl7wAwLe0RtBECUuV96RX9iiU63BP7wI1RQW-G3a1zilI3FHss=" \
        -d '{
                "email":"Vy22@gmail.com",
                "name":"Vy Nguyen",
                "dob":"24/03/1990"
            }'
    ```

- Response
    ```json
    {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": {
             "email":"Vy22@gmail.com",
            "name":"Vy Nguyen",
            "created": 1532886545,
            "dob": 573004800,
            "modified": 1532887465,
            "_id": 13,
        }
    }
    ```

Get an user
- Request
    ```shell
    curl -XGET http://localhost:5000/customer/13 \
        -H "Authorization: gAAAAABV6Cxtz2qbcgOOzcjjyoBXBxJbjxwY2cSPdJB4gta07ZQXUU5NQ2BWAFIxSZlnlCl7wAwLe0RtBECUuV96RX9iiU63BP7wI1RQW-G3a1zilI3FHss=" \
    ```

- Response
    ```json
    {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": {
             "email":"Vy22@gmail.com",
            "name":"Vy Nguyen",
            "created": 1532886545,
            "dob": 573004800,
            "modified": 1532887465,
            "_id": 13,
        }
    }
    ```

Delete an user
- Request
    ```shell
    curl -XDELETE http://localhost:5000/customer/13 \
        -H "Authorization: gAAAAABV6Cxtz2qbcgOOzcjjyoBXBxJbjxwY2cSPdJB4gta07ZQXUU5NQ2BWAFIxSZlnlCl7wAwLe0RtBECUuV96RX9iiU63BP7wI1RQW-G3a1zilI3FHss=" \
    ```

- Response
    ```json
    {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": null
    }
    ```
Get all customers
- Request
    ```shell
    curl -XGET http://localhost:5000/customers \
        -H "Authorization: gAAAAABV6Cxtz2qbcgOOzcjjyoBXBxJbjxwY2cSPdJB4gta07ZQXUU5NQ2BWAFIxSZlnlCl7wAwLe0RtBECUuV96RX9iiU63BP7wI1RQW-G3a1zilI3FHss=" \
    ```

- Response
    ```json
    {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": [
            {
                "name": "Truong Minh Song",
                "created": 1532625319,
                "dob": 638236800,
                "modified": 1532625319,
                "_id": 2,
                "email": "truongminhsong@gmail.com"
            },
            {
                "name": "Truong Minh Song",
                "created": 1532800202,
                "dob": 638236800,
                "modified": 1532800202,
                "_id": 8,
                "email": "truongminhsong21@gmail.com"
            },
            {
                "name": "xx name",
                "created": 1532801050,
                "dob": 638236800,
                "modified": 1532801050,
                "_id": 9,
                "email": "xx@yy.com"
            },
            {
                "name": "Truong Minh Song",
                "created": 1532886257,
                "dob": 638236800,
                "modified": 1532886257,
                "_id": 10,
                "email": "truongminhsong32@gmail.com"
            }
        ]
    }
    ```

Get all customers with pagging and filter
- Request
    ```shell
    curl -XPOST http://localhost:5000/customers \
        -H "Content-Type: application/json" \
        -H "Authorization: gAAAAABV6Cxtz2qbcgOOzcjjyoBXBxJbjxwY2cSPdJB4gta07ZQXUU5NQ2BWAFIxSZlnlCl7wAwLe0RtBECUuV96RX9iiU63BP7wI1RQW-G3a1zilI3FHss=" \
        -d '{
                "page":1,
                "itemPerPage":10,
                "str":"minh"
            }'        
    ```

- Response
    ```json
    {
        "meta": {
            "code": 200,
            "message": "OK"
        },
        "data": {
            "itemPerPage": 10,
            "total": 7,
            "list": [
                {
                    "name": "Truong Minh Song",
                    "created": 1532625319,
                    "dob": 638236800,
                    "modified": 1532625319,
                    "_id": 2,
                    "email": "truongminhsong@gmail.com"
                },
                {
                    "name": "Truong Minh Song",
                    "created": 1532886257,
                    "dob": 638236800,
                    "modified": 1532886257,
                    "_id": 10,
                    "email": "truongminhsong32@gmail.com"
                },
                {
                    "name": "Truong Minh Song",
                    "created": 1532800202,
                    "dob": 638236800,
                    "modified": 1532800202,
                    "_id": 8,
                    "email": "truongminhsong21@gmail.com"
                }
            ],
            "page": 1
        }
    }
    ```
