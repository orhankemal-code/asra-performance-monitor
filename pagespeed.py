import os
import requests

API_KEY = os.environ["PAGESPEED_API_KEY"]

URL = "https://www.asrapirlanta.com"

for strategy in ["mobile", "desktop"]:
    response = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
        params={
            "url": URL,
            "strategy": strategy,
            "key": API_KEY
        }
    )

    data = response.json()

    score = (
        data["lighthouseResult"]["categories"]["performance"]["score"] * 100
    )

    audits = data["lighthouseResult"]["audits"]

    lcp = audits["largest-contentful-paint"]["displayValue"]
    cls = audits["cumulative-layout-shift"]["displayValue"]
    speed_index = audits["speed-index"]["displayValue"]

    print("=" * 50)
    print(strategy.upper())
    print("=" * 50)
    print(f"Performance : {score:.0f}")
    print(f"LCP         : {lcp}")
    print(f"CLS         : {cls}")
    print(f"Speed Index : {speed_index}")
