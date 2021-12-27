import os
import json
from typing import Union

class ScarletUsername:
    def __init__(self, username=None):
        self.value = username
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set username to type {type(other)}")
        else:
            self.value = other
    
    def __len__(self):
        return len(self.value)
    def __str__(self):
        return str(self.value)

class ScarletPassword:
    def __init__(self, password=None):
        self.value = password
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set password to type {type(other)}")
        else:
            self.value = other
    
    def __len__(self):
        return len(self.value)
    def __str__(self):
        return str(self.value)

class ScarletUID:
    def __init__(self, uid=None):
        self.value = uid
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set uid to type {type(other)}")
        else:
            self.value = other
    
    def __len__(self):
        return len(self.value)
    def __str__(self):
        return str(self.value)

class ScarletEmail:
    def __init__(self, email=None):
        self.value = email
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set email to type {type(other)}")
        else:
            self.value = other
    
    def __len__(self):
        return len(self.value)
    def __str__(self):
        return str(self.value)

class ScarletToken:
    def __init__(self, email=None):
        self.value = email
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set token to type {type(other)}")
        else:
            self.value = other
    
    def __len__(self):
        return len(self.value)
    
    def __str__(self):
        return str(self.value)


class ScarletUser:

    attributes: 'list[str]' = [
        "username", "password", "email", "uid", "token"
    ]

    username: 'ScarletUsername' = ScarletUsername()
    password: 'ScarletPassword' = ScarletPassword()
    uid: 'ScarletUID' = ScarletUID()
    email: 'ScarletEmail' = ScarletEmail()
    token: 'ScarletToken' = ScarletToken()


    def __init__(self, *args, **kwargs) -> 'ScarletUser':
        for key in kwargs.keys():
            if key in ScarletUser.attributes:
                setattr(self, key, kwargs[key])

    def __repr__(self):
        desc = ''.join(["\n\t"+ f'{attr}={getattr(self, attr)}' for attr in self.attributes])
        return f"ScarletUser({desc}\n)"
    
    def __dict__(self) -> dict[str, str]:
        return self.normalize()

    def normalize(self) -> dict[str, str]:
        return {
            "username": str(self.username),
            "password": str(self.password),
            "email": str(self.email),
            "token": str(self.token),
            "uid": str(self.uid)
        }

    def export_to_file(self, outfile: str = "./user.json", indent: Union[None, int] = 2):
        filemode = "a" if not os.path.isfile(outfile) else "w"
        with open(outfile, filemode) as file:
            json.dump(self.normalize(), file, indent=indent)

    def create_body(self, attrs: 'list[str]' = []):
        return {attr: str(getattr(self, attr)) for attr in [i for i in attrs if i in ScarletUser.attributes]}

    @staticmethod
    def from_file(filename: str = "./user.json") -> 'ScarletUser':
        if not os.path.isfile(filename):
            raise Exception(f"File: \"{filename}\" could not be located when attempting to get scarlet user from json")
        else:
            with open(filename, 'r') as r:
                return ScarletUser.from_dict(json.load(r))
    
    @staticmethod
    def from_dict(data: dict) -> 'ScarletUser':
        user = ScarletUser()
        for key in data.keys():
            if key in ScarletUser.attributes:
                setattr(user, key, data[key])
        return user