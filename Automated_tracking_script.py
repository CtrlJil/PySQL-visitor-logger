import requests

# URL of the Flask tracking endpoint
TRACKING_URL = "http://localhost:5000/track"

# Send a request to log the visit
response = requests.get(TRACKING_URL)
print("Tracking response:", response.json())
