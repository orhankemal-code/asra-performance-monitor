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
        "performance": int(categories["performance"]["score"] * 100),
        "seo": int(categories["seo"]["score"] * 100),
        "accessibility": int(categories["accessibility"]["score"] * 100),
        "best_practices": int(categories["best-practices"]["score"] * 100),
        "lcp": audits["largest-contentful-paint"]["displayValue"],
        "cls": audits["cumulative-layout-shift"]["displayValue"],
        "speed_index": audits["speed-index"]["displayValue"],
        "fcp": audits["first-contentful-paint"]["displayValue"],
    }
