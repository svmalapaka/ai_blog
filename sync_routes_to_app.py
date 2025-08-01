import os
from datetime import datetime

app_file = "app.py"
routes_folder = "routes"

# 🧠 Load app.py as lines
with open(app_file, "r", encoding="utf-8") as f:
    app_lines = f.readlines()

# 🔍 Detect insertion points
blueprint_index = None
register_index = None
for i, line in enumerate(app_lines):
    if "# 🧩 Blueprints" in line:
        blueprint_index = i
    elif "# 🔗 Register" in line:
        register_index = i

if blueprint_index is None or register_index is None:
    print("⚠️ Injection points not found. Make sure you have '# 🧩 Blueprints' and '# 🔗 Register' in app.py.")
    exit()

# 📦 Discover routes
route_files = [
    f.replace(".py", "")
    for f in os.listdir(routes_folder)
    if f.endswith(".py") and f != "__init__.py"
]

# 🔎 Find existing lines
existing_imports = set()
existing_registrations = set()
for line in app_lines[blueprint_index:register_index]:
    if line.strip().startswith("from routes."):
        existing_imports.add(line.strip())

for line in app_lines[register_index:]:
    if line.strip().startswith("app.register_blueprint("):
        existing_registrations.add(line.strip())

# 🧩 Prepare new lines
new_imports = []
new_regs = []
for route in sorted(route_files):  # alphabetized
    import_line = f"from routes.{route} import {route}"
    register_line = f"app.register_blueprint({route})"

    if import_line not in existing_imports:
        new_imports.append(import_line + "\n")
    if register_line not in existing_registrations:
        new_regs.append(register_line + "\n")

# 💾 Inject new routes
timestamp = f"# Synced on {datetime.now().strftime('%d %B %Y – %I:%M %p')}\n"
injected = False

if new_imports:
    app_lines = (
        app_lines[:blueprint_index + 1]
        + [timestamp] + new_imports
        + app_lines[blueprint_index + 1:]
    )
    injected = True

if new_regs:
    app_lines = (
        app_lines[:register_index + 1]
        + new_regs
        + app_lines[register_index + 1:]
    )
    injected = True

# 🧠 Save updated app.py
if injected:
    with open(app_file, "w", encoding="utf-8") as f:
        f.writelines(app_lines)

    print(f"✅ Synced and injected routes: {', '.join(sorted(route_files))}")
else:
    print("🎉 All routes already present. No injection needed.")