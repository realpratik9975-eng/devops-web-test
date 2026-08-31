import requests

url = "http://localhost:8000/metrics"

response = requests.get(url, timeout=5)

print("HTTP Status:", response.status_code)
print("Response:")
print(response.text)
