from datetime import date
import os

LOG_PATH = "docs/tools_stories"
today = date.today()
slug = today.strftime("%Y-%m-%d-lab-log")
filename = f"{slug}.md"
filepath = os.path.join(LOG_PATH, filename)

if not os.path.exists(filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""---
title: Daily Lab Log
slug: {slug}
date: {today.isoformat()}
author: Sastry Malapaka
tags: [daily, lab, log]
summary: Auto-generated log for {today.strftime('%B %d, %Y')}
---

## 🧪 Daily Metrics Snapshot – {today.strftime('%B %d, %Y')}

This log captures today's metrics and diagnostics.
""")