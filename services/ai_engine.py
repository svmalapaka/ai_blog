def respond_to_user(user_message):
    try:
        # OpenAI path
        import openai
        from config.config import OPENAI_API_KEY
        openai.api_key = OPENAI_API_KEY

        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )
        return completion['choices'][0]['message']['content']

    except Exception as openai_err:
        log_entry("ERROR", f"OpenAI failed: {openai_err}", tags=["AI", "fallback"])

        # Future: Try Copilot here via API call
        # response = call_copilot_api(user_message)
        # return response or fallback

        return "🤖 Sorry, I couldn’t reach the assistant right now. Try again in a moment."