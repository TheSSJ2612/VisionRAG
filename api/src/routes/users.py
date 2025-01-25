from fastapi import APIRouter, HTTPException
from api.src.services.user_services import UserService
from api.src.models.user_model import UserCreate, User
from typing import List

router = APIRouter()
user_service = UserService()


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    return await user_service.create_user(user)


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):  # Added async
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(404, "User not found")
    return {"message": "User deleted"}
