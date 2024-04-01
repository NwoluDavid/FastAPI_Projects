from pydantic import BaseModel, EmailStr,Field, validator
from typing import ClassVar
import re

class UserRegistration(BaseModel):
    username: str = Field(min_length=3, max_length=50, description="Name of user", examples=["John Mac"], title="Name")
    email: EmailStr = Field(description="Email address of the user", example="example@example.com", title="Email")
    password: str = Field(description="User's password", min_length=8, max_length=64, title="Password")

    password_pattern: ClassVar[str] = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-+_!@#$%^&*.,?]).{8,64}$"

    @validator("password")
    def validate_password(cls, v):
        if not re.match(cls.password_pattern, v):
            raise ValueError("Password must contain at least one digit, one lowercase letter, one uppercase letter, one special character, and be between 8 and 64 characters long.")
        return v