# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String, DateTime
# pyrefly: ignore [missing-import]
from sqlalchemy.sql import func
# pyrefly: ignore [missing-import]
from app.db.database import Base
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import relationship
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    company = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    tickets = relationship("Ticket", back_populates="customer")