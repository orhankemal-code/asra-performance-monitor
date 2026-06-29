from datetime import datetime
from pathlib import Path


def save_report(mobile, desktop):
    today = datetime.now().strftime("%Y-%m-%d")

    reports = Path("reports")
    reports.mkdir(exist_ok=True)

    filename = reports / f"{today}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Asra Pırlanta Günlük Performans Raporu\n\n")
        f.write(f"**Tarih:** {today}\n\n")

        f.write("## 📱 Mobile\n\n")
        for key, value in mobile.items():
            f.write(f"- **{key}**: {value}\n")

        f.write("\n## 💻 Desktop\n\n")
        for key, value in desktop.items():
            f.write(f"- **{key}**: {value}\n")

    print(f"Rapor oluşturuldu: {filename}")
