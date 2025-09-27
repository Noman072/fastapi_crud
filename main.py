from fastapi import FastAPI
from api.routers import auth, items

app = FastAPI(
    title="FastAPI Production Ready",
    description="A production-ready FastAPI project with JWT authentication, role-based access, and CRUD operations.",
    version="0.1.0",
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Production Ready API"}
