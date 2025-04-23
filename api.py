from fastapi import FastAPI
from pydantic import BaseModel
from models import load_model, classify_email
from utils import mask_pii, unmask_pii

app = FastAPI()

# Load the model and vectorizer when the app starts
model, vectorizer = load_model()

# Define the input structure for email body
class EmailInput(BaseModel):
    email_body: str

@app.post("/classify_email")
def classify_email_endpoint(email: EmailInput):
    original_text = email.email_body
    # Mask PII in the email
    masked_email, entity_list = mask_pii(original_text)
    # Classify the masked email
    category = classify_email(masked_email, model, vectorizer)
    
    # Return the response in the required format
    return {
        "input_email_body": original_text,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

