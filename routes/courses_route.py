from fastapi import APIRouter
from models.courses_model import Courses

courses_api_router = APIRouter()


@courses_api_router.get("/courses/test")
async def get_test():
    return {"msg": "Hello World"}

@courses_api_router.post("/courses/post")
async def post_test():
    return {"msg": "Hello World"}

@courses_api_router.post("/courses/body")
async def post_test(course:Courses):
    return {"msg": "Hello "+course.name}