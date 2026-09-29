from datetime import datetime
from pydantic import BaseModel


class TicketCreate(BaseModel):
    customer_id: int
    subject: str
    description: str | None = None
    priority: str = "medium"


class TicketOut(BaseModel):
    id: int
    customer_id: int
    subject: str
    description: str | None
    status: str
    priority: str
    created_at: datetime

    class Config:
        from_attributes = True