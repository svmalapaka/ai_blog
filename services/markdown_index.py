import os

TOOLS_PATH = os.path.join(os.getcwd(), 'docs', 'tools_stories')

def generate_md_index():
    from pathlib import Path
    import re
    import frontmatter

    index = []

    for md_path in Path(TOOLS_PATH).glob("*.md"):
        filename = md_path.stem
        try:
            post = frontmatter.load(md_path)
            title = post.get("title", filename.replace("-", " ").title())
            tags = post.get("tags", [])
            match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)", filename)
            date = match.group(1) if match else "Unknown"
            slug = filename
            index.append({
                "date": date,
                "title": title,
                "tags": tags,
                "slug": slug
            })
        except Exception as e:
            print(f"⚠️ Could not parse {filename}: {e}")

    index.sort(key=lambda x: x["date"], reverse=True)
    return index