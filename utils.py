import re

# Function to mask personal identifiable information (PII)
def mask_pii(text):
    # Define regex patterns for each type of PII
    pii_patterns = {
        'full_name': r'\b[A-Z][a-z]*\s[A-Z][a-z]*\b',  # Basic full name pattern (first and last name)
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',  # Email pattern
        'phone_number': r'\+?\d{1,2}?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}',  # Phone number pattern
        'dob': r'\b\d{2}/\d{2}/\d{4}\b',  # Date of birth (MM/DD/YYYY)
        'aadhar_num': r'\b\d{4} \d{4} \d{4}\b',  # Aadhar card number pattern
        'credit_debit_no': r'\b\d{16}\b',  # Credit/Debit card number pattern
        'cvv_no': r'\b\d{3}\b',  # CVV pattern
        'expiry_no': r'\b\d{2}/\d{2}\b',  # Expiry date pattern (MM/YY)
    }

    masked_text = text
    entity_list = []

    # Mask the PII
    for entity, pattern in pii_patterns.items():
        matches = re.finditer(pattern, text)
        for match in matches:
            masked_text = masked_text.replace(match.group(), f'[{entity}]')
            entity_list.append({
                'position': [match.start(), match.end()],
                'classification': entity,
                'entity': match.group()
            })

    return masked_text, entity_list

# Function to unmask PII (for restoring original email if necessary)
def unmask_pii(masked_text, entity_list):
    for entity in entity_list:
        masked_text = masked_text.replace(f'[{entity["classification"]}]', entity["entity"])
    return masked_text
