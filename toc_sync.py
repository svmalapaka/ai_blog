import re
from datetime import datetime
import sys

def generate_toc(markdown_text):
    headers = re.findall(r'^(#{1,6})\s+(.*)', markdown_text, re.MULTILINE)
    toc = []
    for hashes, title in headers:
        level = len(hashes)

        # Clean anchor: strip non-alphanumerics, replace spaces, lowercase
        anchor = re.sub(r'[^\w\s-]', '', title)
        anchor = anchor.replace(' ', '-').lower()

        # Escape display text to prevent HTML issues
        display_title = (
            title.replace('&', '&amp;')
                 .replace('<', '&lt;')
                 .replace('>', '&gt;')
        )

        toc.append(f'{"  " * (level - 1)}- [{display_title}](#{anchor})')
    return '\n'.join(toc)

def inject_toc(html_text, toc_md):
    toc_items = []
    for line in toc_md.splitlines():
        if line.strip() and "](" in line:
            try:
                text = line.split("[")[1].split("]")[0]
                raw_anchor = line.split("](")[1].rstrip(")")
                anchor = re.sub(r'[^\w\-]', '', raw_anchor)
                toc_items.append(f'  <li><a href="#{anchor}">{text}</a></li>')
            except Exception as e:
                print(f"[!] Skipped line due to parse error: {line} — {e}")
    toc_html = '<ul>\n' + '\n'.join(toc_items) + '\n</ul>'

    def replace_block(match):
        return f'<!-- TOC START -->\n{toc_html}\n<!-- TOC END -->'

    updated_html = re.sub(r'<!-- TOC START -->.*?<!-- TOC END -->',
                          replace_block,
                          html_text, flags=re.DOTALL)
    return updated_html

def sync_toc(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    with open(html_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    toc = generate_toc(md_content)
    updated_html = inject_toc(html_content, toc)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    updated_html += f'\n<!-- Synced on {timestamp} -->\n'

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(updated_html)

    print(f"[✓] TOC successfully synced to {html_path} at {timestamp}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        sync_toc(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python toc_sync.py <markdown_path> <html_path>")