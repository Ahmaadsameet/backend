from fastApi import FastAPI

app=FastAPI()
from app.user.route import router as user_router
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}