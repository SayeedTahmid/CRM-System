from fastapi import APIRouter
from firebase_admin import firestore

router = APIRouter()
db = firestore.client()

@router.get("/")
def get_customers():
    customers_ref = db.collection("customers")
    docs = customers_ref.stream()
    customers = [{**doc.to_dict(), "id": doc.id} for doc in docs]
    return {"customers": customers}

@router.post("/")
def create_customer(customer: dict):
    doc_ref = db.collection("customers").add(customer)
    return {"message": "Customer added successfully!", "id": doc_ref[1].id}

