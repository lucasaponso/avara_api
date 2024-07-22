from fastapi import HTTPException, Depends, status, APIRouter, Request, Query
from typing import Annotated
from sqlalchemy.orm import Session
from db_connector.connect import get_db
import db_connector.db_models as db_models
##init of router
router = APIRouter(
    prefix="/example_route"
)

db_dependency = Annotated[Session, Depends(get_db)]

"""
Function Name: getData

Return a string with the parameter that was put into the request

Parameters:
- parameter (str)

"""
@router.get("/get/data", tags=["example_route"], status_code=status.HTTP_200_OK, description="A simple get request to retrieve all data.")
async def getData(author: str, db: db_dependency):
    data = db.query(db_models.books.title).filter(db_models.books.author == author).all()

    if not data:
        return {"message": "No data found"}

    return {title for (title,) in data}

