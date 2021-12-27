from typing import Coroutine
from requests.api import request

from requests.models import ReadTimeoutError

from scarlet.responses import AIResponse, APIResponse
from .scarletuser import *
import requests
import aiohttp
import re


class ScarletCurrentUser:
    def __init__(self):
        self.value = None
    
    def __get__(self, instance, owner):
        return str(self.value)
    def __set__(self, instance, other):
        if type(other) != ScarletUser:
            raise TypeError("Invalid argument type passed. cannot set Scarlet User to anything else besides ScarletUser")
        else:
            self.value = other

class Scarlet:
    base: str = "https://api.scarletai.xyz"

    def __init__(self, user=None):
        self.current_user: 'ScarletUser' = user

    def set_user(self, user: 'ScarletUser' = None):
        """Sets the user for the scarlet instance

        Args:
            user (ScarletUser, optional): [description]. Defaults to None.

        Raises:
            Exception: [description]
        """
        if self.current_user is None:
            self.current_user = user
        else:
            raise Exception("User Has Already Been set")


    @staticmethod
    async def create(username: 'str', password: 'str', email: 'str') -> 'ScarletUser':
        res = requests.post(f"{Scarlet.base}/users", json=True, data={
            "username": username,
            "password": password,
            "email": email
        })

        user = ScarletUser.from_dict({
            **res.json(),
            "password": password,
            "email": email
        })
        print(user)
        return user



    async def docs(self):
        res = requests.get(f"{self.base}/docs")
        regex = re.compile(r"OK. Redirecting to (.+)")
        url = None
        match = re.match(regex, res.text)
        if res.status_code != 200:
            url = "https://github.com/ScarletAI/ScarletAI"
        else:
            if match != None:
                url = match.group(1)
                tmp = requests.get(url)
                if tmp.status_code != 200:
                    url = "https://github.com/ScarletAI/ScarletAI"
            if url is None:
                url = "https://github.com/ScarletAI/ScarletAI"
        return {"url": url}

    async def get_user(self, user_id: str):
        res = requests.get(f"{self.base}/users/{user_id}", json=True, 
            data=self.current_user.create_body(["username", 'password', 'token']))

        print(res.text)
        return res.json()


    async def sentience(self, content: str, ai_token:str = None) -> AIResponse:
        res = requests.post(f"{self.base}/scarlet/analyze", json=True, data={
            "token": ai_token,
            "content": content
        })
        print(res.json())

        return res

