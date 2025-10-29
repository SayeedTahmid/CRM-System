import firebase_admin
from firebase_admin import credentials, firestore

# Load the service account key you just placed
cred = credentials.Certificate("firebase_key.json")

# Initialize Firebase app (only once)
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()
