import abc
from datetime import datetime
from typing import Optional
from ..enums import ZodiacTitle


class BaseHoro(abc.ABC):
    def __init__(self):
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_horoscope(self, sign: ZodiacTitle, date: Optional[datetime] = None):
        raise NotImplementedError()
    
    async def get_compatibility(self, her_sign: ZodiacTitle, his_sign: ZodiacTitle):
        raise NotImplementedError()
