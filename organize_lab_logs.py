import os
import shutil
import re

# 📁 Source folder and destination folder
source_folder = "ai_blog"
dest_folder = os.path.join(source_folder, "markdown_logs")
os.makedirs(dest_folder, exist_ok=True)

# 📄 Files to include (manually curated to avoid test logs)
log_files = [
    "lab_log.md",
    "lab-log-2025-07-14.md",
    "Lab Log — 16 July 2025.txt"
]

# 🔃 Standardize date pattern
def normalize_date(text):
    match = re.search(r"(\d{1,2})\s*(\w+)\s*(2025)", text)
    if match:
        day, month, year = match.groups()
        months = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }
        month_num = months.get(month, "00")
        return f"{year}-{month_num}-{day.zfill(2)}.md"
    return None

# 🛠️ Process and move files
for filename in log_files:
    path = os.path.join(source_folder, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        date = normalize_date(content)
        if date:
            new_path = os.path.join(dest_folder, date)
            with open(new_path, "w", encoding="utf-8") as f_out:
                f_out.write(content)
            print(f"✅ Renamed and moved: {filename} → {date}")
        else:
            print(f"⚠️ Could not extract date from: {filename}")
    else:
        print(f"❌ File not found: {filename}")