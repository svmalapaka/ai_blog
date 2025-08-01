import requests

res = requests.post("http://localhost:8081/event-hook", json={
    "message": "Remote trigger: restarted web service",
    "tags": ["event-hook", "flask", "restart"]
})
print(res.json())