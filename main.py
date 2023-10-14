from fastapi import FastAPI

from app.helper_functions.geocode import get_location, get_route
from app.routers.auth import router as auth_router
from app.routers.user import router as user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)


@app.get('/get_route_by_adress')
def give_route_by_adress(start_point: str, end_point: str):
    start_point_coords = get_location(start_point)
    end_point_coords = get_location(end_point)
    return get_route(start_point_coords, end_point_coords)


@app.get('/get_route_by_coords')
def give_route_by_coords(start_coords: float, end_coords: float):
    return get_route(start_coords, end_coords)
