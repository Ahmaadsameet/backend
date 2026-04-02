from  sqlalchemy import colums ,integers, string
from database import Base

class User(Base):
    __tablename__ = "users"

    id = colum(integers, primary_key=True, index=True)
    email = colum(string, unique=True, index=True)
    password = colum(string)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password
        }