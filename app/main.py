# FastAPI Core + error handling
from fastapi import FastAPI,HTTPException

# import users_collection
from app.database import users_collection

# import Schemas
from app.schemas import UserRegister,UserLogin,ForgetPassword

# import auth files
from app.auth import hash_password,verify_password,create_access_token

# email sending function
from app.email_utils import send_reset_email

from app.auth import get_current_user
from app.database import laptops_collection
from fastapi import Depends

app = FastAPI();

@app.post("/register")
def register(user:UserRegister):
    if users_collection.find_one({"email":user.email}):
        raise HTTPException(status_code=400,detail="Email Already Exists")
    users_collection.insert_one({
        "name":user.name,
        "email":user.email,
        "password":hash_password(user.password)
    })
    return {"message":"Registration Successful"}

@app.post("/login")
def login(user:UserLogin):
    db_user = users_collection.find_one({"email":user.email})
    
    if not db_user or not verify_password(user.password,db_user["password"]):
        raise HTTPException(status_code=401,detail="Invalid credentials")
    
    token = create_access_token({"email":user.email})

    return {"access_token":token,"login":"success"}

@app.post("/forgot-password")
def forgot_password(data:ForgetPassword):
    user = users_collection.find_one({"email":data.email})
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
    token = create_access_token({"email":data.email},expires_minutes=10)
    send_reset_email(data.email,token)
    return {"message":"Password Reset Email Sent Successfully !!!"}

@app.get("/laptops")
def get_laptops(current_user: dict = Depends(get_current_user)):
    laptops = list(laptops_collection.find({}, {"_id": 0}))
    return laptops


