import requests
import sys

url = "http://localhost:9090/api/v1/query"

params = {
    "query": "up"
}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()

except requests.RequestException as e:
    print("ERROR: Could not contact Prometheus")
    print(e)
    sys.exit(1)

print("Prometheus Health Report")
print("------------------------")

failed = False

for result in data["data"]["result"]:

    job = result["metric"]["job"]
    instance = result["metric"]["instance"]
    status = result["value"][1]

    if status == "1":
        status_text = "UP"
    else:
        status_text = "DOWN"
        failed = True

    print(f"{job:12} {instance:20} {status_text}")

if failed:
    print("\nHealth check FAILED")
    sys.exit(1)
else:
    print("\nHealth check PASSED")
    sys.exit(0)
