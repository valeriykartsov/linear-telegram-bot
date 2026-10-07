import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

N8N_URL = os.getenv("N8N_URL")
NGROK_URL = os.getenv("NGROK_URL")
LINEAR_API_KEY = os.getenv("LINEAR_API_KEY")


def check_http(name, url):
    try:
        response = requests.get(url, timeout=5)
        if response.ok:
            print(f"{name}: OK")
            return True

        print(f"{name}: FAIL ({response.status_code})")
        return False

    except requests.RequestException:
        print(f"{name}: FAIL")
        return False


def check_linear():
    try:
        response = requests.post(
            "https://api.linear.app/graphql",
            headers={
                "Authorization": LINEAR_API_KEY,
                "Content-Type": "application/json",
            },
            json={
                "query": "{ viewer { id } }"
            },
            timeout=5,
        )

        if response.ok and not response.json().get("errors"):
            print("Linear: OK")
            return True

        print("Linear: FAIL")
        return False

    except requests.RequestException:
        print("Linear: FAIL")
        return False


checks = [
    check_http("n8n", N8N_URL),
    check_http("ngrok", NGROK_URL),
    check_linear(),
]

if all(checks):
    print("\nHealthcheck: PASS")
    sys.exit(0)

print("\nHealthcheck: FAIL")
sys.exit(1)