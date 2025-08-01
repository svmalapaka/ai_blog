from datetime import datetime
import os

def log_entry(message, tags=None, log_dir="tools"):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    filename = f"{date_str}-lab-log.md"
    filepath = os.path.join(log_dir, filename)

    # Initialize frontmatter if the file doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as log:
            log.write(f"""---
title: Daily Log for {date_str}
date: {date_str}
author: Sastry Malapaka
category: Update
---

""")

    # Append log entry
    tag_line = f"\n**Tags**: {', '.join(tags)}\n" if tags else ""
    entry = f"\n## {date_str} {time_str}\n- {message}{tag_line}"

    with open(filepath, "a", encoding="utf-8") as log:
        log.write(entry)