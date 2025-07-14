# 🧭 Flask Routes for Diagnostics and Logs

---

## 📌 Purpose

Your Flask app isn't just serving pages — it's telling stories about your lab's state, launch status, and learning activity.  
This guide documents key routes used to display real-time diagnostics, logs, and status flags.

---

## 🧩 Route 1: `/launch-status`

### 🚀 Purpose  
Show whether the Flask app and key services are running. This acts like a heartbeat monitor.

### 🔧 How It Works  
- Checks status of Flask server, Markdown engine, Cloudflare tunnel  
- Passes flags to Jinja2 template: `flask_running`, `markdown_ready`, `tunnel_active`  
- Displays status panel with green/red indicators

### 📈 Output Example  
```html
Lab Status ✅  
Tunnel: Active  
Markdown Engine: Ready  
