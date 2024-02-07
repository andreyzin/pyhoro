from pydantic import BaseModel, ConfigDict

from .meta import RamblerMeta


class CompatibilityTopic(BaseModel):
    title: str
    text: str


class Compatibility(BaseModel):
    model_config = ConfigDict(extra="ignore")
    meta: RamblerMeta
    topics: list[CompatibilityTopic]
