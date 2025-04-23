import pickle
from sklearn.ensemble import RandomForestClassifier

# Load the model and vectorizer
def load_model():
    with open('email_classifier_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    return model, vectorizer

# Function to classify an email
def classify_email(email_text, model, vectorizer):
    email_vectorized = vectorizer.transform([email_text])  # Vectorize the input email
    prediction = model.predict(email_vectorized)  # Predict the category
    return prediction[0]
