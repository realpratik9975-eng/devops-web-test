import requests

url = "http://localhost:8000/metrics"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("Application : UP")
        print("HTTP Status :", response.status_code)
    else:
        print("Application : DOWN")
        print("HTTP Status :", response.status_code)

except requests.RequestException as e:
    print("Application : DOWN")
    print("Error        :", e)
