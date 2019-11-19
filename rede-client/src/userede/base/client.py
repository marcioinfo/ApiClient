from userede.base.exceptions import RequestGetError
from userede.base.users import User
from userede.base.environments import Environment, MOCK
import requests
import related
import curlify


@related.immutable
class Access:
    access_token = related.StringField()
    expires_in = related.IntegerField()
    refresh_token = related.StringField()
    scope = related.StringField()
    token_type = related.StringField()


class RedeClient:
    def __init__(self, user: User, environment: Environment):
        self.env = environment
        self.user = user

        if environment == MOCK:
            self.access = Access('', 0, '', '', '')
            self.headers = {'content-type': 'application/json'}
        else:
            r = requests.post(f'{self.env.base_url}/oauth/token',
                              headers={'Content-Type': 'application/x-www-form-urlencoded'},
                              data=f'grant_type=password&username={user.name}&password={user.password}',
                              auth=tuple(user.auth))
            if r.status_code != requests.codes.ok:
                print(curlify.to_curl(r.request))
                raise Exception((r.status_code, r.text))

            self.access = related.from_json(r.text, Access)
            self.headers = {'content-type': 'application/json', 'Authorization': f'{self.access.token_type} {self.access.access_token}'}

    def __repr__(self):
        return f'{self.user} on {self.env}'

    def get(self, endpoint, params: dict):
        r = requests.get(f'{self.env.base_url}{endpoint}', headers=self.headers, params=params)
        if r.status_code != requests.codes.ok:
            print(curlify.to_curl(r.request))
            raise RequestGetError(r.status_code, r.text)
        return r

    def post(self, endpoint, params, data=None):
        r = requests.post(f'{self.env.base_url}{endpoint}', headers=self.headers, params=params, data=data)

        if r.status_code != requests.codes.ok:
            raise RequestGetError(r.status_code, r.text)
        return r

    def put(self, endpoint, params, data=None):
        r = requests.post(f'{self.env.base_url}{endpoint}', headers=self.headers, params=params, data=data)

        if r.status_code != requests.codes.ok:
            raise RequestGetError(r.status_code, r.text)
        return r

