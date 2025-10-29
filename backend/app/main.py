import os
from fastapi import FastAPI
from firebase_admin import credentials, firestore
import firebase_admin
from dotenv import load_dotenv

load_dotenv()  # load variables from .env file

# Get Firebase key path from environment
cred_path = os.getenv("FIREBASE_KEY_PATH")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CRM backend connected to Firebase successfully!"}
