from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    city: str

def user_serializer(user) -> dict:
    return {
        'id': user["id"],
        'name':user["name"],
        'city':user["city"]
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]