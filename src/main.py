from report_writer import save_report
from csv_writer import save_result
from pagespeed import get_pagespeed
# Şimdilik GTmetrix'i devre dışı bırakıyoruz
# from gtmetrix import run_gtmetrix

URL = "https://www.asrapirlanta.com"


def main():
    print("=" * 60)
    print("ASRA PERFORMANCE MONITOR")
    print("=" * 60)

    mobile = get_pagespeed(URL, "mobile")
    desktop = get_pagespeed(URL, "desktop")
    save_result(mobile, desktop)
    save_report(mobile, desktop)

    print("\nMOBILE")
    print(mobile)

    print("\nDESKTOP")
    print(desktop)

    # GTmetrix'i daha sonra ekleyeceğiz
    # print("\nGTMETRIX")
    # print(run_gtmetrix(URL))


if __name__ == "__main__":
    main()
