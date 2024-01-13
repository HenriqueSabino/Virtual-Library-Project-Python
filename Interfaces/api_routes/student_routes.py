from fastapi import APIRouter, Depends, HTTPException
from typing import List
from Core.entities.Student import Student
from UseCases.student_management.CreateStudent import CreateStudent
from UseCases.student_management.UpdateStudent import UpdateStudent
from UseCases.student_management.DeleteStudent import DeleteStudent
from UseCases.student_management.ListStudents import ListStudents

router = APIRouter()

@router.post("/", response_model=Student)
async def create_student(student: Student):
    """
    Create a new student in the system.
    """
    try:
        result = CreateStudent(student).execute()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{student_id}", response_model=Student)
async def update_student(student_id: int, student: Student):
    """
    Update an existing student's information.
    """
    try:
        result = UpdateStudent(student_id, student).execute()
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{student_id}", response_model=Student)
async def delete_student(student_id: int):
    """
    Delete an existing student from the system.
    """
    try:
        result = DeleteStudent(student_id).execute()
        if result is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[Student])
async def list_students():
    """
    List all students in the system.
    """
    try:
        result = ListStudents().execute()
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

```
Please note that in a real-world scenario, you would want to further abstract certain components such as the actual execution of the use case or the handling and raising of HTTP exceptions to make the code more clean and reusable. There may also be additional dependencies related to data access or authorization that would need to be reflected in the route handling.