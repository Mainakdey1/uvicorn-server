import requests


url = "http://127.0.0.1:8000/banks"  

response = requests.get(url)


if response.status_code == 200:
    print("Response Data:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
