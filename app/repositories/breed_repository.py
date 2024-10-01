from sqlalchemy.orm import Session
from app.db.models.breed import Breed
from app.repositories.base_repository import BaseRepository


class BreedRepository(BaseRepository[Breed]):
    def __init__(self):
        super().__init__(Breed)
