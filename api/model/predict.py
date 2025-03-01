import requests
import json

# Replace with your Hugging Face API token
HUGGINGFACE_API_TOKEN = "your_huggingface_api_token"

# List of possible notification types
NOTIFICATION_TYPES = [
    "Informational", "Coupon", "Live Counter", "Email Collector", "Conversions",
    "Conversions Counter", "Video", "Audio", "Social Share"
]

def get_notification_prediction(user_behavior):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Convert user behavior data to a readable string
    behavior_text = json.dumps(user_behavior, indent=2)

    payload = {
        "inputs": f"User behavior: {behavior_text}\n\nWhich notification type is most suitable?",
        "candidate_labels": NOTIFICATION_TYPES
    }
    
    response = requests.post(
        "https://api-inference.huggingface.co/models/facebook/bart-large-mnli",
        headers=headers,
        json=payload
    )
    
    if response.status_code == 200:
        result = response.json()
        
        # Get the highest confidence label
        return result["labels"][0]  
    else:
        error_info = response.json()
        return f"Error: {error_info.get('error', 'unknown error')}, Warnings: {error_info.get('warnings', [])}"