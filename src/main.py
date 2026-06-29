from pagespeed import get_pagespeed

URL = "https://www.asrapirlanta.com"

def main():
    print("=" * 60)
    print("ASRA PERFORMANCE MONITOR")
    print("=" * 60)

    mobile = get_pagespeed(URL, "mobile")
    desktop = get_pagespeed(URL, "desktop")

    print("\nMOBILE")
    print(mobile)

    print("\nDESKTOP")
    print(desktop)


if __name__ == "__main__":
    main()
