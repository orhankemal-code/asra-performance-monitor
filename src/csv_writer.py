import csv
import os
from datetime import datetime

FILE = "reports/pagespeed_history.csv"


def save_result(mobile, desktop):
    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "date",
                "mobile_performance",
                "desktop_performance",
                "mobile_lcp",
                "desktop_lcp",
                "mobile_cls",
                "desktop_cls",
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            mobile["performance"],
            desktop["performance"],
            mobile["lcp"],
            desktop["lcp"],
            mobile["cls"],
            desktop["cls"],
        ])
