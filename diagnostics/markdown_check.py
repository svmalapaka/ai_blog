import markdown

def check_markdown_renderer():
    try:
        test_md = "**Markdown test**"
        html = markdown.markdown(test_md)
        return "✅ Markdown rendering OK" if "<strong>" in html else "❌ Failed to render bold text"
    except Exception as e:
        return f"❌ Markdown check failed: {str(e)}"