from datetime import datetime
from typing import Optional

import httpx

from ..enums import ZodiacTitle
from ..types import Compatibility, Horoscope
from .base import BaseHoro
import hishel


class RamblerHoro(BaseHoro):
    _base_url = "https://horoscopes.rambler.ru/api/front"

    def __init__(self):

        # self._session = httpx.AsyncClient()
        self._session = hishel.AsyncCacheClient(
            storage=hishel.AsyncInMemoryStorage(ttl=60 * 60 * 6, capacity=128),
        )

    async def get_horoscope(self, sign: ZodiacTitle, date: Optional[datetime] = None):
        date = date or datetime.today()

        r = await self._session.get(
            f"{self._base_url}/v1/horoscope/{date.strftime('%Y-%m-%d')}/{sign}",
            follow_redirects=True,
            extensions={"force_cache": True},
        )
        return Horoscope.model_validate(r.json())

    async def get_compatibility(self, her_sign: ZodiacTitle, his_sign: ZodiacTitle):
        r = await self._session.get(
            f"{self._base_url}/v3/horoscope/compatibility/woman-{her_sign}/man-{his_sign}/",
            follow_redirects=True,
            extensions={"force_cache": True},
        )
        data = r.json()
        topics = []
        topic = {"title": "Главное", "text": ""}
        for i in data["content"]["text"]:
            if i["type"] == "paragraph":
                topic["text"] += "\n\n" * bool(topic["text"]) + i["content"]

            elif i["type"].startswith("header"):
                topics.append(topic)
                topic = {"title": i["content"], "text": ""}

        topics.append(topic)
        return Compatibility.model_validate({"meta": data["meta"], "topics": topics})
