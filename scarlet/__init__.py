from .scarletuser import *
import requests



class Scarlet:
    base: str = "https://api.scarletai.xyz"

    def __init__(self, *args, **kwargs):
        self.current_user: 'ScarletUser' = None

    def set_user(self, user: 'ScarletUser' =None):
        self.current_user = user

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
        return user

    async def docs(self):
        res = requests.get(f"{self.base}/docs")
        print(res.text)

    async def get_user(self, user_id: str):
        res = requests.get(f"{self.base}/users/{user_id}", json=True, 
            data=self.current_user.create_body(["username", 'password', 'token']))

        print(res.text)
        return res.json()


    async def sentience(self, content: str, ai_token:str = None):
        res = requests.post(f"{self.base}/scarlet/analyze", json=True, data={
            "token": ai_token,
            "content": content
        })
        print(res.json())

        return res

