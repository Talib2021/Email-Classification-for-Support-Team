# Email Classification for Support Team  

## Overview  
This project implements an email classification system for support teams, featuring:  
1. **PII Masking**: Detects and masks sensitive information (e.g., names, emails, credit card numbers) using regex.  
2. **Email Classification**: Uses a `RandomForestClassifier` trained on TF-IDF vectorized email text to categorize emails into 4 classes: `Incident`, `Request`, `Problem`, `Change`.  
3. **API Deployment**: FastAPI endpoint that accepts an email and returns the masked text, PII entities, and predicted category.  

## Setup  
1. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt

   Run the API locally:

uvicorn api:app --reload
Access the API at http://127.0.0.1:8000/docs for interactive testing.

Deploy on Hugging Face Spaces:

Add api.py, models.py, utils.py, and model files (*.pkl) to a Space.

Configure the Space to use FastAPI (example Dockerfile provided in the repo).

API Usage
Send a POST request to /classify_email with JSON payload:

{
  "email_body": "My name is John Doe. My email is john@example.com. I need help with my account."
}
Response Format:


{
  "input_email_body": "Original email text",
  "list_of_masked_entities": [
    {"position": [start, end], "classification": "full_name", "entity": "John Doe"},
    {"position": [start, end], "classification": "email", "entity": "john@example.com"}
  ],
  "masked_email": "My name is [full_name]. My email is [email]...",
  "category_of_the_email": "Request"
}
Files
api.py: FastAPI endpoint.

models.py: Loads the trained model and vectorizer.

utils.py: PII masking/unmasking logic.

email_classifier_model.pkl, vectorizer.pkl: Pretrained model files.

run using the command -  python -m uvicorn api:app --reload