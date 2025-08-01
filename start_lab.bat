@echo off
cd /d "C:\Users\svmal\ai_blog"
call venv\Scripts\activate.bat
start "Cloudflare Tunnel" cmd /k cloudflared tunnel run mvsastry-tunnel
python app.py
pause