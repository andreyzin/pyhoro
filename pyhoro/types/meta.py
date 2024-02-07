from pydantic import BaseModel


class RamblerMeta(BaseModel):
    title: str
    description: str
    keywords: str
    og_image: str
    twitter_image: str
    vk_image: str
