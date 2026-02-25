from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserRegister (BaseModel):
    username: str = Field (min_length=5)
    email: EmailStr
    age: int = Field (ge=18)

user_info = {'username': 'ranjansood711', 'email': 'ranjansood711@gmail.com', 'age': '26'}

try:
    user_1 = UserRegister(**user_info)
    print("Registration Successful:")
    print(user_1.model_dump())
except ValidationError as e:
    print("Registration Rejected! Errors found:")
    print(e.json())