from pydantic import BaseModel


class ModelResponse(BaseModel):
    label: str
    score: float