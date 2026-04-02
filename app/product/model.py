from sqlalcemy import Column, Integer, String, Float
from app.database import Base

class product(Base):
        __tablename__ = "product"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, unique=True, index=True)
        description = Column(String)
        price = Column(Float)

        def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "price": self.price
            }