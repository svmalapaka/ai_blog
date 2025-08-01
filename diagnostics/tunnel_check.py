import requests

def test_tunnel_connection():
    try:
        response = requests.get("https://your-tunnel-url.com/chat", timeout=3)
        return "✅ Tunnel active" if response.status_code == 200 else f"❌ Tunnel unreachable ({response.status_code})"
    except Exception as e:
        return f"❌ Tunnel test failed: {str(e)}"