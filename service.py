import falcon
import json
import datetime
import jwt

secret_key = 'ocr123'

class ThingsResource(object):

    # def on_post(self, req, resp):
    #
    #     # body = req.stream.read()
    #     # request = json.loads(body)
    #     request = json.loads(req.stream.read())
    #
    #     """Handles GET requests"""
    #     resp.status = falcon.HTTP_200
    #     b = {
    #      'msg': 'Two things awe me most, the starry sky'
    #     }
    #     resp.body = json.dumps(b, ensure_ascii=False)

    def on_post(self, req, resp):
        print("Enter")
        request = json.loads(req.stream.read())
        payload = {
            'userId': request['userId'],
            'password': request['password'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            'iat': datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            'nbf': datetime.datetime.utcnow()
        }
        # token = JWTAuthBackend.sign(self, user_payload=payload)
        token = "jwt " + jwt.encode(payload, secret_key).decode('utf-8')
        resp.body = json.dumps({'token': token}, ensure_ascii=False)
        resp.status = falcon.HTTP_200


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/service', things)
