from fastapi import FastAPI

from api.geocode import get_location, get_route

app = FastAPI(
    redoc_url=None,
    docs_url='/api/v1/docs'
)


@app.get('/get_route')
def give_route(start_point: str, end_point: str):
    start_point1 = get_location(start_point)
    end_point1 = get_location(end_point)
    print(get_route(start_point1, end_point1))
    return get_route(start_point1, end_point1)
