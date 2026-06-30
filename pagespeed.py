import os
import time
import json
import requests

API_KEY = os.environ["PAGESPEED_API_KEY"]

API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def get_pagespeed(url, strategy):

    params = [
        ("url", url),
        ("strategy", strategy),
        ("key", API_KEY),
        ("category", "performance"),
        ("category", "accessibility"),
        ("category", "best-practices"),
        ("category", "seo"),
    ]

    for attempt in range(3):

        try:

            print(f"\n==============================")
            print(f"{strategy.upper()} TESTİ ({attempt+1}/3)")
            print("==============================")

            response = requests.get(
                API_URL,
                params=params,
                timeout=120
            )

            print("\nİSTEK URL")
            print(response.url)

            response.raise_for_status()

            data = response.json()

            print("\n========== FULL RESPONSE ==========")
            print(json.dumps(data, indent=2))
            print("===================================")

            categories = data["lighthouseResult"]["categories"]
            audits = data["lighthouseResult"]["audits"]

            print("\nKategori Anahtarları:")
            print(list(categories.keys()))

            return {
                "performance": int(categories.get("performance", {}).get("score", 0) * 100),
                "seo": int(categories.get("seo", {}).get("score", 0) * 100),
                "accessibility": int(categories.get("accessibility", {}).get("score", 0) * 100),
                "best_practices": int(categories.get("best-practices", {}).get("score", 0) * 100),
                "lcp": audits.get("largest-contentful-paint", {}).get("displayValue", "-"),
                "fcp": audits.get("first-contentful-paint", {}).get("displayValue", "-"),
                "cls": audits.get("cumulative-layout-shift", {}).get("displayValue", "-"),
                "speed_index": audits.get("speed-index", {}).get("displayValue", "-"),
            }

        except Exception as e:

            print(f"\nHATA ({strategy})")
            print(e)

            if attempt < 2:
                print("\n20 saniye bekleniyor...\n")
                time.sleep(20)
            else:
                print("\nPageSpeed API başarısız oldu.\n")

                return {
                    "performance": -1,
                    "seo": -1,
                    "accessibility": -1,
                    "best_practices": -1,
                    "lcp": "-",
                    "fcp": "-",
                    "cls": "-",
                    "speed_index": "-",
                }
