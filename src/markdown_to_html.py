from htmlnode import HTMLNode
from markdown_parser import markdown_to_blocks, block_to_block_type, text_to_textnodes
from conversion import text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def handle_paragraph(block):
    return HTMLNode("p", children=text_to_children(block))

def handle_heading(block):
    level = block.count('#')
    text = block[level+1:].strip()
    return HTMLNode(f"h{level}", children=text_to_children(text))

def handle_code(block):
    code_text = "\n".join(block.split('\n')[1:-1])
    return HTMLNode("pre", children=[HTMLNode("code", value=code_text)])

def handle_quote(block):
    quote_text = "\n".join(line[2:] for line in block.split('\n'))
    return HTMLNode("blockquote", children=text_to_children(quote_text))

def handle_unordered_list(block):
    items = block.split('\n')
    children = [HTMLNode("li", children=text_to_children(item[2:])) for item in items]
    return HTMLNode("ul", children=children)

def handle_ordered_list(block):
    items = block.split('\n')
    children = [HTMLNode("li", children=text_to_children(item[3:])) for item in items]
    return HTMLNode("ol", children=children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":
            html_nodes.append(handle_paragraph(block))
        elif block_type == "heading":
            html_nodes.append(handle_heading(block))
        elif block_type == "code":
            html_nodes.append(handle_code(block))
        elif block_type == "quote":
            html_nodes.append(handle_quote(block))
        elif block_type == "unordered_list":
            html_nodes.append(handle_unordered_list(block))
        elif block_type == "ordered_list":
            html_nodes.append(handle_ordered_list(block))

    return HTMLNode("div", children=html_nodes)