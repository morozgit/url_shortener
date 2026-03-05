from pydantic import BaseModel, HttpUrl


class LinkAdd(BaseModel):
    original_url: HttpUrl


class LinkAddResponse(BaseModel):
    short_url: str


class LinkStatsResponse(BaseModel):
    clicks: int


class Link(BaseModel):
    id: int
    original_url: HttpUrl
    short_url: str
    clicks: int

    model_config = {
        "from_attributes": True
    }