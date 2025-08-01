def check_copilot_status():
    try:
        # Example placeholder logic
        response = {"widget_visible": True, "message_flow": "✅ OK"}
        return "✅ Copilot widget initialized and responsive" if response["widget_visible"] else "❌ Widget not found"
    except Exception as e:
        return f"❌ Copilot status check failed: {str(e)}"