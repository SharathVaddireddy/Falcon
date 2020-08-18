import jwt
import json
import datetime
import falcon
import mongoengine as mongo
from settings import middleware, dbcfg
# secret_key = 'ocr123'
db = mongo.connect(
    'development',  # This will be the name of your database
    host=dbcfg['host'],
    port=dbcfg['port'],
    username=dbcfg['username'],
    password=dbcfg['password']
)


class ApiResource:
    # token auth backend

    @classmethod
    def on_post(cls, req, resp):
        authorized = req.context['user']
        print(authorized['user']['userId'])
        resp.body = "This resource uses token authentication"

    @classmethod
    def on_get(cls, req, resp):
        resp.body = "This resource doesn't need authentication"


class AuthenticateResource:
    # print("Entered class")

    def __init__(self):
        self.secret_key = 'ocr123'

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        print("Entered class")

        request = json.loads(req.stream.read())
        payload = {
            'userId': request['userId'],
            'password': request['password'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            'iat': datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            'nbf': datetime.datetime.utcnow()
        }
        # token = JWTAuthBackend.sign(self, user_payload=payload)
        token = "jwt " + jwt.encode(payload, self.secret_key).decode('utf-8')
        resp.body = json.dumps({'token': token}, ensure_ascii=False)
        resp.status = falcon.HTTP_200


def initialize() -> falcon.API:
    print("in Initialize")
    """
    Initialize the falcon api and our router
    :return: an initialized falcon.API
    """
    api = falcon.API(media_type='application/json', middleware=middleware)

    api.add_route("/api", ApiResource())
    api.add_route("/authenticate", AuthenticateResource())
    return api


# def run():
#     print("in run")
#     return initialize()

run = initialize()