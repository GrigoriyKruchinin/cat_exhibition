from app.db.models.breed import Breed as BreedModel
from app.repositories.base_repository import BaseRepository


class BreedRepository(BaseRepository[BreedModel]):
    def __init__(self):
        super().__init__(BreedModel)
