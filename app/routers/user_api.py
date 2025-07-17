from fastapi import APIRouter

router = APIRouter(prefix="/api/users", tags=["Users"])

# GET /api/users/
@router.get("/")
def get_users():
    return [{"id": 1, "name": "Anh Tuấn"}]

# POST /api/users/
@router.post("/")
def create_user(user: dict):
    return {"message": "User created", "data": user}
