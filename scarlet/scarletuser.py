import os
import json
from typing import Union

class ScarletValue:
    def __init__(self, value=None):
        self.value = value
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set value to type {type(other)}")
        else:
            self.value = other
    
    def __len__(self):
        return len(self.value)
    def __str__(self):
        return str(self.value)

class ScarletUsername(ScarletValue):
    def __init__(self, username=None):
        super().__init__(username)
    
    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set username to type {type(other)}")
        else:
            self.value = other
    

class ScarletPassword(ScarletValue):
    def __init__(self, password=None):
        super().__init__(password)

    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set password to type {type(other)}")
        else:
            self.value = other

class ScarletUID(ScarletValue):
    def __init__(self, uid=None):
        super().__init__(uid)

    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set uid to type {type(other)}")
        else:
            self.value = other

class ScarletEmail(ScarletValue):
    def __init__(self, email=None):
        super().__init__(email)

    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set email to type {type(other)}")
        else:
            self.value = other

class ScarletToken(ScarletValue):
    def __init__(self, token=None):
        super().__init__(token)

    def __set__(self, instance, other):
        if type(other) != str:
            raise TypeError(f"Cannot Set token to type {type(other)}")
        else:
            self.value = other


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
        """creates a dictionary containing the same info as the ScarletUser

        Returns:
            dict[str, str]: dictionary contianing user info
        """
        return {
            "username": str(self.username),
            "password": str(self.password),
            "email": str(self.email),
            "token": str(self.token),
            "uid": str(self.uid)
        }

    def export_to_file(self, outfile: str = "./user.json", indent: Union[None, int] = 2):
        """exports user info to a file

        Args:
            outfile (str, optional): the file to export to. Defaults to "./user.json".
            indent (Union[None, int], optional): this just changes the indent spacing of the json set None to disable. Defaults to 2.
        """
        filemode = "a" if not os.path.isfile(outfile) else "w"
        with open(outfile, filemode, encoding="utf-8") as file:
            json.dump(self.normalize(), file, indent=indent, ensure_ascii=False)

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