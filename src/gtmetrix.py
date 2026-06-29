import os
import time
import requests

API_KEY = os.getenv("GTMETRIX_API_KEY")

BASE_URL = "https://gtmetrix.com/api/2.0/tests"


def run_gtmetrix(url):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(
        BASE_URL,
        headers=headers,
        json={
            "url": url
        },
        timeout=60,
    )

    response.raise_for_status()

    test = response.json()

    test_id = test["id"]

    while True:
        result = requests.get(
            f"{BASE_URL}/{test_id}",
            headers=headers,
            timeout=60,
        )

        result.raise_for_status()

        data = result.json()

        state = data["state"]

        if state == "completed":
            break

        time.sleep(5)

    return {
        "grade": data["results"]["grade"],
        "performance": data["results"]["performance_score"],
        "structure": data["results"]["structure_score"],
        "lcp": data["results"]["largest_contentful_paint"],
    }
