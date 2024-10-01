from sqlalchemy.orm import Session
from app.repositories.base_repository import BaseRepository
from typing import TypeVar, Generic

T = TypeVar("T")


class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, id: int):
        return self.repository.get_by_id(db, id)

    def create(self, db: Session, obj_in: T):
        return self.repository.create(db, obj_in)

    def update(self, db: Session, db_obj: T, obj_in: dict):
        return self.repository.update(db, db_obj, obj_in)

    def delete(self, db: Session, id: int):
        return self.repository.delete(db, id)
