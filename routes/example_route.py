from fastapi import HTTPException, Depends, status, APIRouter, Request, Query
from typing import Annotated
from sqlalchemy.orm import Session
from db_connector.connect import get_db
import db_connector.db_models as db_models
from pydantic import BaseModel, EmailStr, Field
##init of router
router = APIRouter(
    prefix="/example_route"
)

db_dependency = Annotated[Session, Depends(get_db)]


class userCred(BaseModel):
    username: str
    password: str

"""
Function Name: getData

Return a string with the parameter that was put into the request

Parameters:
- parameter (str)
"""
@router.post("/get/token", tags=["example_route"], status_code=status.HTTP_200_OK, description="A simple get request to retrieve all data.")
async def getData(user_creds: userCred, db: db_dependency):
    # Check if username and password exist in the database
    user = db.query(db_models.user).filter(db_models.user.username == user_creds.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    # Validate password (for demonstration purposes; use proper hashing and verification in production)
    if user.password != user_creds.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    # Hash password


    # Here, you would typically generate a token and return it
    # For demonstration purposes, let's assume a simple message
    return {"token": "dummy_token"}