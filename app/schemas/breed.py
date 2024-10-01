from pydantic import BaseModel


class BreedBase(BaseModel):
    name: str
    description: str | None = None


class BreedCreate(BreedBase):
    pass


class Breed(BreedBase):
    id: int

    class ConfigDict:
        from_attributes = True
