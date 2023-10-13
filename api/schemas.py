from pydantic import BaseModel


class RouteModel(BaseModel):
    start_point: str
    end_point: str
