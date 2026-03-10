from fastapi import FastAPI, status
from routes.healthy_check import router as health_checker
from routes.hospitals import router as hospitals_router



app = FastAPI(title="RxManager API")

@app.get("/")
async def root() -> str:
    return "API is running"


app.include_router(health_checker)

app.include_router(hospitals_router)