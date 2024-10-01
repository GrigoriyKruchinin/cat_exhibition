from pydantic import BaseModel


class KittenBase(BaseModel):
    name: str
    color: str
    age_months: int
    description: str | None = None


class KittenCreate(KittenBase):
    breed_id: int


class Kitten(KittenBase):
    id: int
    breed_id: int

    class ConfigDict:
        from_attributes = True
