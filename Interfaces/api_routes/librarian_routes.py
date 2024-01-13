from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..core.use_cases.interfaces.ILibrarianRepository import ILibrarianRepository
from ..core.entities.Librarian import Librarian

librarian_router = APIRouter()

@librarian_router.post("/librarians", response_model=Librarian, status_code=status.HTTP_201_CREATED)
async def create_librarian(librarian: Librarian, librarian_repository: ILibrarianRepository = Depends()):
    return await librarian_repository.add_librarian(librarian)

@librarian_router.get("/librarians/{librarian_id}", response_model=Librarian)
async def get_librarian(librarian_id: int, librarian_repository: ILibrarianRepository = Depends()):
    librarian = await librarian_repository.get_librarian_by_id(librarian_id)
    if librarian is None:
        raise HTTPException(status_code=404, detail="Librarian not found")
    return librarian

@librarian_router.put("/librarians/{librarian_id}", response_model=Librarian)
async def update_librarian(librarian_id: int, librarian: Librarian, librarian_repository: ILibrarianRepository = Depends()):
    return await librarian_repository.update_librarian(librarian_id, librarian)

@librarian_router.delete("/librarians/{librarian_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_librarian(librarian_id: int, librarian_repository: ILibrarianRepository = Depends()):
    await librarian_repository.remove_librarian(librarian_id)
    return {"message": "Librarian deleted"}

@librarian_router.get("/librarians", response_model=List[Librarian])
async def list_librarians(librarian_repository: ILibrarianRepository = Depends()):
    return await librarian_repository.list_librarians()