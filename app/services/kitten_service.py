from sqlalchemy.orm import Session
from app.repositories.kitten_repository import KittenRepository
from app.schemas.kitten import KittenCreate as KittenCreateSchema
from app.db.models.kitten import Kitten as KittenModel
from app.services.base_service import BaseService


class KittenService(BaseService[KittenModel]):
    def __init__(self):
        super().__init__(KittenRepository())

    def create_kitten(self, db: Session, kitten_data: KittenCreateSchema):
        kitten = KittenModel(**kitten_data.model_dump())
        return self.repository.create(db, kitten)

    def get_kittens_by_breed(self, db: Session, breed_id: int):
        return self.repository.get_by_breed(db, breed_id)
