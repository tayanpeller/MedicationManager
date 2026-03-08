from fastapi import FastAPI, status


app = FastAPI(title="RxManager API")

@app.get("/")
async def root() -> str:
    return "API is running"


@app.get("/check", status_code=status.HTTP_200_OK)
async def healthy_check():
    return {"STATUS": "healthy"}