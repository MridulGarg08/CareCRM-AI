# pyrefly: ignore [missing-import]

# Pydantic is used to validate the data coming from API requests.
from pydantic import BaseModel

# pyrefly: ignore [missing-import]
from fastapi import HTTPException

# FastAPI is used to create our REST API.
# pyrefly: ignore [missing-import]
from fastapi import FastAPI

# Import the database engine and SQLAlchemy Base.
# engine = connection to the database
# Base = parent class that keeps track of our database models
# pyrefly: ignore [missing-import]
from app.db.database import engine, Base

# Import the customer model.
#
# This may look unused, but it is important.
# Importing customer.py causes Python to load the Customer
# SQLAlchemy model and register it with Base.
# pyrefly: ignore [missing-import]
from app.models import customer, tickets

# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
# pyrefly: ignore [missing-import]
from fastapi import Depends

# pyrefly: ignore [missing-import]
from app.db.database import get_db

# pyrefly: ignore [missing-import]
from app.models.customer import Customer

# pyrefly: ignore [missing-import]
from app.schemas.customer import CustomerCreate, CustomerOut

# pyrefly: ignore [missing-import]
from app.models.tickets import Ticket

# pyrefly: ignore [missing-import]
from app.schemas.ticket import TicketCreate, TicketOut


# ---------------------------------------------------------
# Pydantic Customer Model
# ---------------------------------------------------------
# This Customer class is NOT the database table.
# It is used to validate incoming API request data.
#
# Example request:
# {
#     "name": "Mridul",
#     "email": "mridul@example.com"
# }
#
# FastAPI will check that name and email are provided
# and are strings.

# ---------------------------------------------------------
# Create FastAPI Application
# ---------------------------------------------------------
app = FastAPI(title="CareCRM AI")

# ---------------------------------------------------------
# Create Database Tables
# ---------------------------------------------------------
# SQLAlchemy checks all the models registered with Base
# and creates their corresponding tables in the database.
#
# If the table already exists, it will NOT delete it
# and will NOT create a duplicate table.
#
# For now this is fine while we are developing the project.
# Later, we can use Alembic for proper database migrations.
Base.metadata.create_all(bind=engine)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/greet/{name}")
def greet(name:str):
    return {"message":f"Hello {name},Welcome to CareCRM AI"}


# FastAPI uses our Pydantic Customer model above
# to validate the incoming request.
#
# NOTE:
# Currently this endpoint only receives the customer
# and returns a response.
# It does NOT save the customer to the database yet.

@app.get("/api/customers", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()


@app.get("/api/customers/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.post("/api/customers", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        company=customer.company,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

# @app.post("/api/customers")
# def createCustomer(customer:Customer):
#     return {"message":f" Customer Received:{customer.name} , {customer.email}"}

@app.get("/api/search")
def searchCustomer(q:str="", db: Session = Depends(get_db)):
    customers = db.query(Customer).filter(Customer.name.ilike(f"%{q}%")).all()
    return customers

@app.post("/api/tickets", response_model=TicketOut)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


@app.get("/api/customers/{customer_id}/tickets", response_model=list[TicketOut])
def get_customer_tickets(customer_id: int, db: Session = Depends(get_db)):
    return db.query(Ticket).filter(Ticket.customer_id == customer_id).all()
