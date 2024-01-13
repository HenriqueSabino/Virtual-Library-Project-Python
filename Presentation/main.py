from fastapi import FastAPI
from .dependencies import get_query_token, get_token_header
from .api_routes import book_routes, student_routes, librarian_routes, administrator_routes, authentication_routes

app = FastAPI(dependencies=[Depends(get_query_token)])

# Include the routers from the different domains
app.include_router(book_routes.router)
app.include_router(student_routes.router)
app.include_router(librarian_routes.router)
app.include_router(administrator_routes.router)
app.include_router(authentication_routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Virtual Library!"}