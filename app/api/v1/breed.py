from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.breed_service import BreedService
from app.db.session import get_db
from app.schemas.breed import BreedCreate, Breed

router = APIRouter()
breed_service = BreedService()


@router.post("/", response_model=Breed)
def create_breed(breed_data: BreedCreate, db: Session = Depends(get_db)):
    return breed_service.create_breed(db, breed_data)


@router.get("/", response_model=list[Breed])
def get_all_breeds(db: Session = Depends(get_db)):
    return breed_service.get_all(db)


@router.get("/{breed_id}", response_model=Breed)
def get_breed(breed_id: int, db: Session = Depends(get_db)):
    breed = breed_service.get_by_id(db, breed_id)
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed


@router.put("/{breed_id}", response_model=Breed)
def update_breed(breed_id: int, breed_data: BreedCreate, db: Session = Depends(get_db)):
    breed = breed_service.get_by_id(db, breed_id)
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed_service.update(db, breed, breed_data.model_dump())


@router.delete("/{breed_id}", response_model=Breed)
def delete_breed(breed_id: int, db: Session = Depends(get_db)):
    breed = breed_service.delete(db, breed_id)
    if breed is None:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed
