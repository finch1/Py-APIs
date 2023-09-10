from enum import Enum
from pydantic import BaseModel
from typing import Optional


class PostType(Enum):
    FOOD = "food"
    TRAVEL = "travel"
    MUSIC = "music"

class Post(BaseModel):
    # : str = throws error if k v not present or content not of defined type
    # in other words, we are defining the schema which the client should send
    title: str
    content: str
    # with default value i.e. if content is not provided
    published: bool = True
    rating: Optional[int] = None
    postType: PostType

