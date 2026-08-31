import os

environment = os.getenv("APP_ENV")
api_url = os.getenv("API_URL")
api_token = os.getenv("API_TOKEN")

print("Environment :", environment)
print("API URL     :", api_url)
print("API Token   :", api_token)
