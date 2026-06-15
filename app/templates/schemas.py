from enum import Enum

from pydantic import BaseModel


class Channel(str, Enum):
    email = "email"
    sms = "sms"
    push = "push"


class CreateTemplateRequest(BaseModel):
    name: str
    channel: Channel
    subject: str | None = None
    body: str


class TemplateResponse(BaseModel):
    id: str
    created_at: str
    name: str
    channel: Channel
    subject: str | None = None
    body: str


class PaginatedTemplatesResponse(BaseModel):
    page: int
    page_size: int
    data: list[TemplateResponse]
