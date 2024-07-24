from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from uuid import UUID
from datetime import datetime


class BlogResponse(BaseModel):
    id: UUID
    author_id: UUID
    title: str
    content: str
    image_url: Optional[str]
    tags: Optional[List[str]]
    is_deleted: bool
    excerpt: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Blog(BaseModel):

    author_id: str
    title: str
    content: str
    image_url: Optional[str]
    is_deleted: bool
    excerpt: Optional[str]
    tags: Optional[List[str]]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
