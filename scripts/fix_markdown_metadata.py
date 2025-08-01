import os
import frontmatter

TOOLS_PATH = os.path.join(os.getcwd(), 'docs', 'tools_stories')
DEFAULT_AUTHOR = "Sastry Venkata Malapaka"

def sanitize_tags(tags_raw):
    if isinstance(tags_raw, list):
        return [str(tag).strip() for tag in tags_raw if tag]
    elif isinstance(tags_raw, str):
        return [tag.strip() for tag in tags_raw.replace('[','').replace(']','').split(',') if tag.strip()]
    else:
        return []

def fix_file(path):
    print(f"🔍 Checking: {os.path.basename(path)}")

    with open(path, 'r', encoding='utf-8') as f:
        try:
            post = frontmatter.load(f)
            fixed = False

            # Fix missing or malformed metadata
            if not post.get('title'):
                post['title'] = os.path.basename(path).replace('.md', '').replace('_', ' ').title()
                fixed = True

            if not post.get('tags') or isinstance(post['tags'], str):
                post['tags'] = sanitize_tags(post.get('tags', ""))
                fixed = True

            if not post.get('author'):
                post['author'] = DEFAULT_AUTHOR
                fixed = True

            if fixed:
                with open(path, 'w', encoding='utf-8') as fw:
                    fw.write(frontmatter.dumps(post))
                print(f"✅ Fixed: {os.path.basename(path)}")
            else:
                print("👌 Metadata already valid.")

        except Exception as e:
            print(f"⚠️ Failed to parse: {os.path.basename(path)} ➤ {e}")

def run_validator():
    for fname in os.listdir(TOOLS_PATH):
        if fname.endswith('.md'):
            fix_file(os.path.join(TOOLS_PATH, fname))

if __name__ == "__main__":
    run_validator()