from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Kitten(Base):
    __tablename__ = "kittens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    color = Column(String)
    age_months = Column(Integer)
    description = Column(String)
    breed_id = Column(Integer, ForeignKey("breeds.id"))

    breed = relationship(
        "Breed", back_populates="kittens", primaryjoin="Kitten.breed_id == Breed.id"
    )
