from pydantic import BaseModel


class InputRequest(BaseModel):
    text: str


class Response(BaseModel):
    predicted_class: str
