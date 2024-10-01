from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.kitten_service import KittenService
from app.db.session import get_db
from app.schemas.kitten import (
    KittenCreate as KittenCreateSchema,
    Kitten as KittenSchema,
)

router = APIRouter()
kitten_service = KittenService()


@router.post("/", response_model=KittenSchema)
def create_kitten(kitten_data: KittenCreateSchema, db: Session = Depends(get_db)):
    """
    Создает нового котенка.

    - **kitten_data**: Данные для создания котенка.
    """
    return kitten_service.create_kitten(db, kitten_data)


@router.get("/", response_model=list[KittenSchema])
def get_all_kittens(db: Session = Depends(get_db)):
    """
    Получает список всех котят.
    """
    return kitten_service.get_all(db)


@router.get("/{kitten_id}", response_model=KittenSchema)
def get_kitten(kitten_id: int, db: Session = Depends(get_db)):
    """
    Получает информацию о котенке по его идентификатору.

    - **kitten_id**: Идентификатор котенка.
    - Возвращает 404, если котенок не найден.
    """
    kitten = kitten_service.get_by_id(db, kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten


@router.put("/{kitten_id}", response_model=KittenSchema)
def update_kitten(
    kitten_id: int, kitten_data: KittenCreateSchema, db: Session = Depends(get_db)
):
    """
    Обновляет данные котенка по его идентификатору.

    - **kitten_id**: Идентификатор котенка.
    - **kitten_data**: Данные для обновления котенка.
    - Возвращает 404, если котенок не найден.
    """
    kitten = kitten_service.get_by_id(db, kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten_service.update(db, kitten, kitten_data.model_dump())


@router.delete("/{kitten_id}", response_model=dict)
def delete_kitten(kitten_id: int, db: Session = Depends(get_db)):
    """
    Удаляет котенка по его идентификатору.

    - **kitten_id**: Идентификатор котенка.
    - Возвращает 404, если котенок не найден.
    """
    kitten = kitten_service.delete(db, kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return {"message": "Kitten successfully deleted"}


@router.get("/breed/{breed_id}", response_model=list[KittenSchema])
def get_kittens_by_breed(breed_id: int, db: Session = Depends(get_db)):
    """
    Получает список котят по идентификатору породы.

    - **breed_id**: Идентификатор породы.
    """
    return kitten_service.get_kittens_by_breed(db, breed_id)
