from fastapi import APIRouter, HTTPException

from app.account.models import User
from app.auth.auth import user_dependency
from app.database import db_dependency
from app.helper_functions.geocode import get_location, get_route

router = APIRouter(
    tags=['user']
)


@router.get("/all_users")
def get_all_users(db: db_dependency):
    return db.query(User).all()


@router.get("/users_address")
def get_address(user: user_dependency, db: db_dependency, friend_id: int):
    friend = db.query(User).filter(User.id == friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    friend_address = friend.current_address
    return {"friend_address": friend_address}


@router.get("/go_to_user")
def go_to_user(user: user_dependency, db: db_dependency, friend_id: int):
    user = db.query(User).filter(User.id == user['id']).first()
    user_address = user.current_address

    friend = db.query(User).filter(User.id == friend_id).first()
    if not friend:
        raise HTTPException(status_code=404, detail="Friend not found")
    friend_address = friend.current_address

    user_coords = get_location(user_address)
    friend_coords = get_location(friend_address)
    return get_route(user_coords, friend_coords)
