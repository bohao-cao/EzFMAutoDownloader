__author__ = 'bcao'
from urllib import request
from urllib import error
import os
from base64 import b64encode

class BoxContentApiAdapter:

    def authorize(username, secret):
        state = os.urandom(16)
        url = 'https://app.box.com/api/oauth2/authorize?response_type=code&client_id='
        + username + '&state=' + b64encode(state).decode('utf-8')
        try:
            response = request.urlopen(url)
            print(response)
            return response
        except error.HTTPError as err:
            print(err.code)

        except Exception as inst:
            print(type(inst))


