import pydantic

class User(pydantic.BaseModel):
    name: str
    phone: int
    year: int

    def __str__(self):
        return f"{self.name}"


user = User(name="name", phone=111, year=2010)
user_data = user.model_dump()
print(user_data)
print(user)
# data = {"name": "name", "phone": 111, "year": 111}
# user = User(**data)
# json_data = '{"name": "name", "phone": 111, "year": 111}'
# user = User.model_validate_json(json_data)
