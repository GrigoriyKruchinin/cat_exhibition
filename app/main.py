from fastapi import FastAPI
from app.api.v1 import breed, kitten

app = FastAPI()

app.include_router(breed.router, prefix="/breeds", tags=["Breeds"])
app.include_router(kitten.router, prefix="/kittens", tags=["Kittens"])
