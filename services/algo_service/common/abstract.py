from pydantic import BaseModel


class InvestItem(BaseModel):
    name: str
    country: str
    id: str
