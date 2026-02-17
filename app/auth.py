from dotenv import load_dotenv
load_dotenv()

from jose import JWSError,jwt
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# encrypt the password & verification
from passlib.context import CryptContext

# expire time
from datetime import datetime,timedelta
# create the token
from jose import jwt
# read variables from env file
import os
# define bcrypt
# pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
pwd_context = CryptContext(
    schemes=["bcrypt"],
    bcrypt__rounds=12,
    deprecated="auto"
)
# read SECRETE_KEY
SECRETE_KEY = os.getenv("SECRET_KEY")
# read ALGORITHM
ALGORITHM = os.getenv("ALGORITHM")

# def hash_password(password:str):
#     return pwd_context.hash(password)

def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])  # bcrypt safety

def verify_password(password,hashed):
    return pwd_context.verify(password,hashed)

def create_access_token(data:dict,expires_minutes:int=30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRETE_KEY,algorithm=ALGORITHM)

def decode_access_token(token:str):
    try:
        payload = jwt.decode(token,SECRETE_KEY, algorithms=[ALGORITHM])
        return payload
    except JWSError:
        return None

def get_current_user(token: str = Depends(oauth2_schema)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
    return payload