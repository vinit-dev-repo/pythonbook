# Optional: python -m pip install pydantic==2.14.1
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

p = Person.model_validate({"name": "Amy", "age": 28})   # validates automatically
print(p)
print(p.model_dump_json())                               # straight to JSON
