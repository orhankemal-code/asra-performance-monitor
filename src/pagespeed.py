import os
import requests

API_KEY = os.getenv("PAGESPEED_API_KEY")

API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def get_pagespeed(url, strategy):

    response = requests.get(
        API_URL,
        params={
            "url": url,
            "strategy": strategy,
            "key": API_KEY,
        },
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    audits = data["lighthouseResult"]["audits"]

    categories = data["lighthouseResult"]["categories"]

return {
    "performance": int(categories.get("performance", {}).get("score", 0) * 100),
    "seo": int(categories.get("seo", {}).get("score", 0) * 100),
    "accessibility": int(categories.get("accessibility", {}).get("score", 0) * 100),
    "best_practices": int(categories.get("best-practices", {}).get("score", 0) * 100),
    "lcp": audits.get("largest-contentful-paint", {}).get("displayValue", "-"),
    "cls": audits.get("cumulative-layout-shift", {}).get("displayValue", "-"),
    "speed_index": audits.get("speed-index", {}).get("displayValue", "-"),
    "fcp": audits.get("first-contentful-paint", {}).get("displayValue", "-"),
}
