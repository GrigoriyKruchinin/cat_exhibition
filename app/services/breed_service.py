from sqlalchemy.orm import Session
from app.repositories.breed_repository import BreedRepository
from app.schemas.breed import BreedCreate
from app.services.base_service import BaseService
from app.db.models.breed import Breed as BreedModel


class BreedService(BaseService[BreedModel]):
    def __init__(self):
        super().__init__(BreedRepository())

    def create_breed(self, db: Session, breed_data: BreedCreate):
        breed = BreedModel(**breed_data.model_dump())
        return self.repository.create(db, breed)
