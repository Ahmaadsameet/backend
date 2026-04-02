
from app.user.repositories import Repo

repo= Repo()

class Service:

    def __init__(self):
        self.repo = repo

    def login_user(self, user: dict):
        for u in self.repo.users:
            if u["email"] == user["email"] and u["password"] == user["password"]:
                return {"message": "Login successful"}
        return {"message": "User not found"}

    def create_user(self, user: dict):
        for u in self.repo.users:
            if u["email"] == user["email"]:
                return {"message": "User already exists"}
        self.repo.users.append(user)
        return user
