from fastapi import HTTPException, Depends, status, APIRouter, Request, Query
##init of router
router = APIRouter(
    prefix="/example_route"
)

"""
Function Name: getData

Return a string with the parameter that was put into the request

Parameters:
- parameter (str)

"""
@router.get("/get/data", tags=["example_route"], status_code=status.HTTP_200_OK, description="A simple get request to retrieve all data.")
async def getData(parameter: str):
    return f"Getting data: {parameter}"
