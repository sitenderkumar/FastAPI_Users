from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer
from model import User, user_serializer, users_serializer
from db import collection
from auth import VerifyToken

app = FastAPI()
auth_token = HTTPBearer()

    
@app.get("/getuser")
def getuser():
    users = users_serializer(collection.find())
    return {"status": "Ok","data": users}

@app.get("/getuser/{id}")
def getuser(id: int):
    try:
        user = user_serializer(collection.find_one({"id": id}))
    except:
        return {"status": 404, "data": "User not found"}
    return {"status": "Ok","data": user}

@app.post("/createuser", status_code=201)
def createuser(user: User, token: str = Depends(auth_token)):
    authorized = VerifyToken(token.credentials).verify()
    if authorized.get("status")=="error":
         raise HTTPException(status_code=400, detail="Not authorized")
    try:
        doc = collection.find_one({"id": user.id})
        if doc:
            return {"status": 400, "data": "User ID already exists"}
    except:
        pass
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": user}

@app.put("/updateuser/{id}")
def updateuser(id: int, user: User, token: str = Depends(auth_token), ):
    authorized = VerifyToken(token.credentials).verify()
    if authorized.get("status")=="error":
         raise HTTPException(status_code=400, detail="Not authorized")
    
    oldDoc = collection.find_one_and_update(
        {"id": id}, 
        {"$set": dict(user)}
    )
    if not oldDoc: 
        return {"status": 404, "data": "User not found"}
    user = user_serializer(collection.find_one({"id": user.id}))
    return {"status": "Ok","data": user}

@app.delete("/deleteuser/{id}")
def deleteuser(id: int, token: str = Depends(auth_token), ):
    authorized = VerifyToken(token.credentials).verify()
    if authorized.get("status")=="error":
         raise HTTPException(status_code=400, detail="Not authorized")
    
    deleted = collection.find_one_and_delete(
        {"id": id}
    )
    if not deleted: 
        return {"status": 404, "data": "User not found"}
    return {"status": "Ok","data": []}