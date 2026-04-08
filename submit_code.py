import os
import requests
import json

token = os.environ.get("ACMOJ_TOKEN")
problem_id = 1448
with open("src.hpp", "r") as f:
    code = f.read()

api_base = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}

data = {"language": "cpp", "code": code}
response = requests.post(f"{api_base}/problem/{problem_id}/submit", headers=headers, data=data)
print(response.json())
