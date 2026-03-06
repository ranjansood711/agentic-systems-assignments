from pydantic import BaseModel, Field, EmailStr, ValidationError, ConfigDict
from typing import Optional

class Address (BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    city: str = Field (min_length=3)
    pincode: str = Field (min_length=6, max_length=6, pattern=r'^\d{6}$')

class User (BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    user_id: int
    name: str
    email: EmailStr
    age: int = Field (ge=18)
    address: Address
    is_premium: Optional[bool] = False

try:
    valid_address = Address(city="Mumbai", pincode="400001")
    user = User(
        user_id=101,
        name="Alice",
        email="alice@example.com",
        age=25,
        address=valid_address
        )
    print(f"Success! User created: {user.name}, Age: {user.age}")
except ValidationError as e:
    print(e)

try:
    bad_address = Address(city="Delhi", pincode="1100AA") # Fails the regex pattern
except ValidationError as e:
    print("Caught Error:")
    print(e.errors()[0]['msg'])

try:
    # Using the valid user from Test 1
    print(f"Attempting to change {user.name}'s age from {user.age} to 16...")
    user.age = 16  # This will trigger the assignment validation
except ValidationError as e:
    print("Caught Error:")
    print(e.errors()[0]['msg'])