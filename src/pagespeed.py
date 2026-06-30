import os
import time
import json
import requests

API_KEY = os.environ["PAGESPEED_API_KEY"]

API_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def get_pagespeed(url, strategy):

    for attempt in range(3):

        try:

            print(f"\n{strategy.upper()} testi başlatılıyor... ({attempt+1}/3)")

            response = requests.get(
                API_URL,
                params={
                    "url": url,
                    "strategy": strategy,
                    "key": API_KEY
                },
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            if "lighthouseResult" not in data:
                print("API beklenmeyen cevap döndürdü:")
                print(json.dumps(data, indent=2))
                raise Exception("lighthouseResult bulunamadı.")

            categories = data["lighthouseResult"]["categories"]
            audits = data["lighthouseResult"]["audits"]

            print("\n========== CATEGORIES ==========")
            print(json.dumps(categories, indent=2))
            print("================================\n")

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
                print("20 saniye sonra tekrar denenecek...\n")
                time.sleep(20)
            else:
                print("PageSpeed API cevap vermedi veya geçersiz veri döndürdü.")

                return {
                    "performance": -1,
                    "seo": -1,
                    "accessibility": -1,
                    "best_practices": -1,
                    "lcp": "-",
                    "fcp": "-",
                    "cls": "-",
                    "speed_index": "-"
                }
