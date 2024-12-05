
import math


class Repository:
    def __init__(self, url: str) -> None:
        self._url = url
    
    @property
    def url(self):
        return self._url
    
    @property
    def pi(self):
        return math.pi
    

