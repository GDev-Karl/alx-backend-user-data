import base64
import requests

# The username and password
username = 'my_username'
password = 'my_password'

# Create the credentials string
credentials = f"{username}:{password}"

# Encode the credentials string using Base64
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

# Create the Authorization header
headers = {
    'Authorization': f'Basic {encoded_credentials}'
}

# Send a GET request with the Authorization header
response = requests.get('https://api.example.com/protected-resource', headers=headers)

# Print the response
print(response.status_code)
print(response.text)
