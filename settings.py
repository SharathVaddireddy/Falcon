import os
import falcon_jsonify
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
import pymongo

dbcfg = {
    'host': 'localhost',  # or external server address
    'port': 27017,
    'username': os.environ.get(''),
    'password': os.environ.get(''),
}

# my_client = pymongo.MongoClient("mongodb://localhost:27017/")
# my_db = my_client["iteqorchestrator"]
# my_col = my_db["user"]
#
# # x = mycol.find_one()
# mydict = {"userId": "BBOKYA01", "password": "1234", "role": "bau"}

# x = my_col.insert_one(mydict)
# print(x)

secret_key = 'ocr123'
user_loader = lambda user: {'user': user}
auth_backend = JWTAuthBackend(user_loader, secret_key)
auth_middleware = FalconAuthMiddleware(
    auth_backend,
    exempt_routes=['/authenticate'],
    exempt_methods=['HEAD'])

middleware = [
    auth_middleware
]
