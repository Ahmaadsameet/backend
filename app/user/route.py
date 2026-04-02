from fastapi import APIRouter
from app.user.service import Service

router = APIRouter()

service = Service()


@router.post("/signup")
def create_user(user: dict):
    return service.create_user(user)

@router.post("/login")
def login_user(user: dict):
    return service.login_user(user)