from sqlalchemy.orm import Session
from app.db.models.kitten import Kitten
from app.repositories.base_repository import BaseRepository


class KittenRepository(BaseRepository[Kitten]):
    def __init__(self):
        super().__init__(Kitten)

    def get_by_breed(self, db: Session, breed_id: int):
        return db.query(Kitten).filter(Kitten.breed_id == breed_id).all()
