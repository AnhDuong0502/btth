from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Query

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online",
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline",
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online",
    },
]
app = FastAPI()


@app.get("/courses")
def get_all_courses():
    return {"message": "Lấy danh sách khóa học thành công", "data": courses}


@app.get("/courses/search")
def filter_course(
    mode: Optional[str] = Query(None, description="Lọc theo hình thức khóa học:off/on"),
    category: Optional[str] = Query(
        None, description="Lọc theo nhóm khóa học:FE và BE"
    ),
):
    result = courses
    if mode:
        result = [course for course in result if course["mode"] == mode]

    if category:
        result = [course for course in result if course["category"] == category]

    return result


@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return {"Message": "Chi tiết khóa học", "data": course}

    raise HTTPException(status_code=404, detail="Không tìm thấy khóa học")
