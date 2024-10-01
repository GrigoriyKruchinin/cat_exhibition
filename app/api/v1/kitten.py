from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.kitten_service import KittenService
from app.db.session import get_db
from app.schemas.kitten import KittenCreate, Kitten

router = APIRouter()
kitten_service = KittenService()


@router.post("/", response_model=Kitten)
def create_kitten(kitten_data: KittenCreate, db: Session = Depends(get_db)):
    return kitten_service.create_kitten(db, kitten_data)


@router.get("/", response_model=list[Kitten])
def get_all_kittens(db: Session = Depends(get_db)):
    return kitten_service.get_all(db)


@router.get("/{kitten_id}", response_model=Kitten)
def get_kitten(kitten_id: int, db: Session = Depends(get_db)):
    kitten = kitten_service.get_by_id(db, kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten


@router.put("/{kitten_id}", response_model=Kitten)
def update_kitten(
    kitten_id: int, kitten_data: KittenCreate, db: Session = Depends(get_db)
):
    kitten = kitten_service.get_by_id(db, kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten_service.update(db, kitten, kitten_data.model_dump())


@router.delete("/{kitten_id}", response_model=Kitten)
def delete_kitten(kitten_id: int, db: Session = Depends(get_db)):
    kitten = kitten_service.delete(db, kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten


@router.get("/breed/{breed_id}", response_model=list[Kitten])
def get_kittens_by_breed(breed_id: int, db: Session = Depends(get_db)):
    return kitten_service.get_kittens_by_breed(db, breed_id)
