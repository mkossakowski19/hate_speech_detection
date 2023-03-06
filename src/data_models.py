from pydantic import BaseModel, validator


class InputRequest(BaseModel):
    text: str

    @validator("text", pre=True, always=True)
    def check_text(cls, value):
        if not isinstance(value, str):
            raise ValueError("Text field must be a string")
        return value


class Response(BaseModel):
    predicted_class: str
