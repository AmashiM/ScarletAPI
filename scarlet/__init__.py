from typing import Coroutine
from requests.api import request

from requests.models import ReadTimeoutError

from scarlet.responses import AIResponse, APIResponse, DocsResponse
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

    _docs_regex = re.compile(r"OK. Redirecting to (http.+)")

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
    def sync_create(username: 'str', password: 'str', email: 'str') -> 'ScarletUser':
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

    @staticmethod
    async def create(username: 'str', password: 'str', email: 'str') -> 'ScarletUser':
        async with aiohttp.ClientSession() as session:
            async with session.post(url=f"{Scarlet.base}/users", data={
                "username": username,
                "password": password,
                "email": email
            }) as res:
                print(res.status)
                if res.status == 200:
                    return ScarletUser(await res.json())
                else:
                    raise Exception("returned unknown status code")

    async def docs(self) -> 'DocsResponse':
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base}/docs") as res:
                url: str = None
                if res.status != 200:
                    url: str = "https://github.com/ScarletAI/ScarletAI"
                else:
                    txt: str = await res.text("utf-8")
                    match = re.match(self._docs_regex, txt)
                    if match != None:
                        url: str = match.group(1)
                        async with session.get(url) as tmp:
                            if tmp.status != 200:
                                url: str = "https://github.com/ScarletAI/ScarletAI"
                        if url is None:
                            url: str = "https://github.com/ScarletAI/ScarletAI"
                return DocsResponse({'url': url})


    def sync_docs(self):
        res = requests.get(f"{self.base}/docs")
        url = None
        match = re.match(self._docs_regex, res.text)
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
        async with aiohttp.ClientSession() as session:
            async with session.get(url=f"{self.base}/users/{user_id}",
                data=self.current_user.create_body(["username", 'password', 'token'])) as res:
                return res.json()

    def sync_get_user(self, user_id: str):
        res = requests.get(f"{self.base}/users/{user_id}", json=True, 
            data=self.current_user.create_body(["username", 'password', 'token']))
        return res.json()

    async def sentience(self, content: str, ai_token: str = None) -> AIResponse:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=f"{self.base}/scarlet/analyze", data={
            "token": ai_token,
            "content": content
        }) as res:
                return AIResponse(await res.json())

    def sync_sentience(self, content: str, ai_token:str = None) -> AIResponse:
        res = requests.post(f"{self.base}/scarlet/analyze", json=True, data={
            "token": ai_token,
            "content": content
        })

        return AIResponse(res.json())
