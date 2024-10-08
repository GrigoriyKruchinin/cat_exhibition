from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.breed_service import BreedService
from app.db.session import get_db
from app.schemas.breed import BreedCreate as BreedCreateSchema, Breed as BreedSchema

router = APIRouter()
breed_service = BreedService()


@router.post("/", response_model=BreedSchema)
def create_breed(breed_data: BreedCreateSchema, db: Session = Depends(get_db)):
    """
    Создает новую породу.

    - **breed_data**: Данные для создания породы.
    """
    return breed_service.create_breed(db, breed_data)


@router.get("/", response_model=list[BreedSchema])
def get_all_breeds(db: Session = Depends(get_db)):
    """
    Получает список всех пород.
    """
    return breed_service.get_all(db)


@router.get("/{breed_id}", response_model=BreedSchema)
def get_breed(breed_id: int, db: Session = Depends(get_db)):
    """
    Получает информацию о породе по ее идентификатору.

    - **breed_id**: Идентификатор породы.
    - Возвращает 404, если порода не найдена.
    """
    breed = breed_service.get_by_id(db, breed_id)
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed


@router.put("/{breed_id}", response_model=BreedSchema)
def update_breed(
    breed_id: int, breed_data: BreedCreateSchema, db: Session = Depends(get_db)
):
    """
    Обновляет данные породы по ее идентификатору.

    - **breed_id**: Идентификатор породы.
    - **breed_data**: Данные для обновления породы.
    - Возвращает 404, если порода не найдена.
    """
    breed = breed_service.get_by_id(db, breed_id)
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed_service.update(db, breed, breed_data.model_dump())


@router.delete("/{breed_id}", response_model=dict)
def delete_breed(breed_id: int, db: Session = Depends(get_db)):
    """
    Удаляет породу по ее идентификатору.

    - **breed_id**: Идентификатор породы.
    - Возвращает 404, если порода не найдена.
    """
    breed = breed_service.delete(db, breed_id)
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return {"message": "Breed successfully deleted"}
