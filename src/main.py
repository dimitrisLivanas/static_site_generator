import os
from textnode import TextNode

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

def main():
    # Existing functionality
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

    # New functionality to copy static files
    src_dir = 'static'
    dest_dir = 'public'
    copy_static(src_dir, dest_dir)

if __name__ == "__main__":
    main()