from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from Core.entities.Administrator import Administrator
from UseCases.admin_management.CreateAdministrator import CreateAdministrator
from UseCases.admin_management.UpdateAdministrator import UpdateAdministrator
from UseCases.admin_management.DeleteAdministrator import DeleteAdministrator
from UseCases.admin_management.ListAdministrators import ListAdministrators

# This could be a dependency that provides the specific use case classes
# For simplicity, they are initiated directly in the routes here
create_administrator_uc = CreateAdministrator(...)
update_administrator_uc = UpdateAdministrator(...)
delete_administrator_uc = DeleteAdministrator(...)
list_administrators_uc = ListAdministrators(...)

router = APIRouter()

@router.post("/", response_model=Administrator, status_code=status.HTTP_201_CREATED)
def create_administrator(admin_data: Administrator):
    try:
        new_admin = create_administrator_uc.execute(admin_data)
        return new_admin
    except Exception as e:  # Better exception handling would be applied in real code
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{admin_id}", response_model=Administrator)
def update_administrator(admin_id: int, admin_data: Administrator):
    try:
        updated_admin = update_administrator_uc.execute(admin_id, admin_data)
        return updated_admin
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{admin_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_administrator(admin_id: int):
    try:
        delete_administrator_uc.execute(admin_id)
        return {"message": "Administrator deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=List[Administrator])
def list_administrators():
    try:
        admins = list_administrators_uc.execute()
        return admins
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))