import os

# Define base folder
BASE_DIR = os.path.join(os.getcwd(), "lab_manifest")

# Define folder structure
folders = [
    "docs",
    "config",
    "modules",
    "routes",
    "blueprints"
]

# Define files with starter content
files = {
    "docs/lab_overview.md": "# 🧠 Lab Overview\n\nThis file summarizes the full lab setup and structure.",
    "docs/python_portal.md": "# 🐍 Python Portal\n\nNotes and logic extracted from mvsastry.dev/python-portal.",
    "config/settings.yaml": "lab_name: AI Learning Lab\nsecure: true\nmarkdown_rendering: enabled",
    "config/env_flags.yaml": "debug: false\nuse_ssl: true\ngeo_visuals: true",
    "modules/__init__.py": "# Init for Python modules",
    "routes/route_map.md": "# 🌐 Flask Route Map\n\nList of endpoints and their corresponding views.",
    "blueprints/module_index.md": "# 📦 Module Index\n\nDocumented Python modules and logic patterns."
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

# Create files with content
for path, content in files.items():
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Lab manifest folder created and initialized.")