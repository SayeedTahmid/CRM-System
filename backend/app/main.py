from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CRM backend connected to Firebase successfully!"}

from app.api import customers
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
