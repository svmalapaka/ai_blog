import os

# 📁 Where your Markdown files live
md_folder = os.path.join("docs", "tools_stories")

# 🧩 Routes you want to scaffold
routes = [
    "ai_in_finance",
    "ai_in_healthcare",
    "ai_in_hr",
    "ai_in_marketing",
    "ai_in_education",
    "ai_in_ethics",
    "ai_in_supplychain"
]

# 🛠️ Create folder if missing
os.makedirs(md_folder, exist_ok=True)

# 🔁 Generate missing .md files
created = []
for route in routes:
    md_path = os.path.join(md_folder, f"{route}.md")
    if not os.path.exists(md_path):
        with open(md_path, "w", encoding="utf-8") as f:
            title = route.replace("_", " ").title()
            f.write(f"# {title}\n\n")
            f.write("🚧 This page is under construction. Soon you'll find insights on how AI transforms this domain.\n")
        created.append(route)

# 📋 Summary
if created:
    print(f"✅ Created placeholder files for: {', '.join(created)}")
else:
    print("🎉 All topic files already exist. No new files created.")