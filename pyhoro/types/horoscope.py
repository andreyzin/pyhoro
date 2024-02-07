from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from ..enums import ZodiacTitle
from .meta import RamblerMeta

class HoroscopeSign(BaseModel):
    id: int
    slug: ZodiacTitle
    name: str
    dates: str


class Horoscope(BaseModel):
    model_config = ConfigDict(extra="ignore")
    title: str = Field(alias="h1")
    seo_text: Optional[str]
    meta: RamblerMeta
    source: str
    text: str
    sign: HoroscopeSign
