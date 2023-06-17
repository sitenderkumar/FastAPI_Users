from fastapi import FastAPI, HTTPException
from model import User, user_serializer, users_serializer
from db import collection

app = FastAPI()

    
@app.get("/getuser")
def getuser():
    users = users_serializer(collection.find())
    return {"status": "Ok","data": users}

@app.get("/getuser/{id}")
def getuser(id: int):
    try:
        user = user_serializer(collection.find_one({"id": id}))
    except:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "Ok","data": user}

@app.post("/createuser", status_code=201)
def createuser(user: User):
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": user}

@app.put("/updateuser/{id}")
def updateuser(id: int, user: User):
    oldDoc = collection.find_one_and_update(
        {"id": id}, 
        {"$set": dict(user)}
    )
    if not oldDoc: raise HTTPException(status_code=404, detail="User not found")
    user = user_serializer(collection.find_one({"id": user.id}))
    return {"status": "Ok","data": user}

@app.delete("/deleteuser/{id}")
def deleteuser(id: int):
    deleted = collection.find_one_and_delete(
        {"id": id}
    )
    if not deleted: raise HTTPException(status_code=404, detail="User not found")
    return {"status": "Ok","data": []}