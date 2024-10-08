from fastapi import FastAPI
from app.routes import router as student_router

app = FastAPI()

app.include_router(student_router, tags=["Student"], prefix="/student")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Student Database API"}
