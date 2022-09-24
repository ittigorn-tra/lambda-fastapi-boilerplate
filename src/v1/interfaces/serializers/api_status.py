from pydantic import BaseModel


class ApiStatusSerializer(BaseModel):
    title: str
    description: str
    version: str
