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
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    categories = data["lighthouseResult"]["categories"]
    audits = data["lighthouseResult"]["audits"]

    performance = int(categories["performance"]["score"] * 100)
    seo = int(categories["seo"]["score"] * 100)
    accessibility = int(categories["accessibility"]["score"] * 100)
    best_practices = int(categories["best-practices"]["score"] * 100)

    lcp = audits["largest-contentful-paint"]["displayValue"]
    cls = audits["cumulative-layout-shift"]["displayValue"]
    speed_index = audits["speed-index"]["displayValue"]
    fcp = audits["first-contentful-paint"]["displayValue"]

    print("=" * 60)
    print(strategy.upper())
    print("=" * 60)

    print(f"Performance    : {performance}")
    print(f"SEO            : {seo}")
    print(f"Accessibility  : {accessibility}")
    print(f"Best Practices : {best_practices}")

    print()

    print(f"LCP            : {lcp}")
    print(f"FCP            : {fcp}")
    print(f"CLS            : {cls}")
    print(f"Speed Index    : {speed_index}")

    print()
    print("Categories JSON:")
    print(categories)
