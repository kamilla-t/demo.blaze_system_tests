
import requests

from helpers.b64helper import convert_to_b64


class UserApi():

    @staticmethod
    def create_user(login, password):
        r = requests.post(url="https://api.demoblaze.com/signup", json={"username": login, "password": convert_to_b64(password)})
        return r
