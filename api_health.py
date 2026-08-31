import requests

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=5)

    print("HTTP Status:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        print("API Status : UP")
        print("API Name   :", data.get("current_user_url"))

    else:
        print("API Status : DOWN")

except requests.RequestException as e:
    print("API Status : DOWN")
    print("Error      :", e)
