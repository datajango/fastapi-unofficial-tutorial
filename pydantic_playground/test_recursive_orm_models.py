from typing import List
from pydantic import BaseModel

def test_recursive_orm_models():
    class PetCls:
        def __init__(self, *, name: str, species: str):
            self.name = name
            self.species = species


    class PersonCls:
        def __init__(self, *, name: str, age: float = None, pets: List[PetCls]):
            self.name = name
            self.age = age
            self.pets = pets


    class Pet(BaseModel):
        name: str
        species: str

        class Config:
            orm_mode = True


    class Person(BaseModel):
        name: str
        age: float = None
        pets: List[Pet]

        class Config:
            orm_mode = True


    bones = PetCls(name='Bones', species='dog')
    orion = PetCls(name='Orion', species='cat')
    anna = PersonCls(name='Anna', age=20, pets=[bones, orion])
    anna_model = Person.from_orm(anna)

    assert anna_model.name == 'Anna'
    assert anna_model.age ==20.0
    assert anna_model.pets == [
        Pet(name='Bones', species='dog'),
        Pet(name='Orion', species='cat')
    ]
