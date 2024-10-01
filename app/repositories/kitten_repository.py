from sqlalchemy.orm import Session
from app.db.models.kitten import Kitten as KittenModel
from app.repositories.base_repository import BaseRepository


class KittenRepository(BaseRepository[KittenModel]):
    def __init__(self):
        super().__init__(KittenModel)

    def get_by_breed(self, db: Session, breed_id: int):
        return db.query(KittenModel).filter(KittenModel.breed_id == breed_id).all()
