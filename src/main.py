import os
from textnode import TextNode
from markdown_to_html import markdown_to_html_node

def copy_static(src, dest):
    if os.path.exists(dest):
        for root, dirs, files in os.walk(dest, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    os.makedirs(dest, exist_ok=True)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_static(s, d)
        else:
            with open(s, 'rb') as fsrc:
                with open(d, 'wb') as fdst:
                    fdst.write(fsrc.read())
            print(f"Copied {s} to {d}")

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    # Read template file
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders in template
    full_html = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

    # Write the full HTML to dest_path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path).replace('.md', '.html')
                generate_page(from_path, template_path, dest_path)

def main():
    # Existing functionality
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

    # New functionality to copy static files
    src_dir = 'static'
    dest_dir = 'public'
    copy_static(src_dir, dest_dir)

    # Generate pages recursively
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()