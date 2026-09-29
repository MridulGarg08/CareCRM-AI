from datetime import datetime
from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None
    company: str | None = None


class CustomerOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None
    company: str | None
    created_at: datetime

    class Config:
        from_attributes = True