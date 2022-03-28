from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class FetchService():

    def __init__(self):
        pass

    def fetchJson(self, endpoint: str, parameters, headers): 

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(endpoint, params=parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            raise
  