from typing import Union

class APIResponse:
    status: 'int'
    data: 'Union[str, dict]'
    def __init__(self, **data: 'dict') -> 'APIResponse':
        for key in data.keys():
            setattr(self, key, data[key])

class AIResponse:
    message: str
    score: int
    flagged: bool
    status: int
    words: 'list[str]'
    raw: dict
    _attrs = ['score', 'flagged', 'status', 'words', 'message']
    def __init__(self, data: dict) -> "AIResponse":
        for key in data.keys():
            setattr(self, key)
        self.raw = data
        