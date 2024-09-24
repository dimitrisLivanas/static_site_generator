import unittest
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_paragraph(self):
        markdown = "This is a paragraph."
        html_node = markdown_to_html_node(markdown)
        expected = HTMLNode("div", children=[HTMLNode("p", children=[HTMLNode(None, value="This is a paragraph.")])])
        self.assertEqual(html_node.to_html(), expected.to_html())

    def test_markdown_to_html_heading(self):
        markdown = "# This is a heading"
        html_node = markdown_to_html_node(markdown)
        expected = HTMLNode("div", children=[HTMLNode("h1", children=[HTMLNode(None, value="This is a heading")])])
        self.assertEqual(html_node.to_html(), expected.to_html())

    def test_markdown_to_html_code(self):
        markdown = "```\nThis is a code block\n```"
        html_node = markdown_to_html_node(markdown)
        expected = HTMLNode("div", children=[HTMLNode("pre", children=[HTMLNode("code", value="This is a code block")])])
        self.assertEqual(html_node.to_html(), expected.to_html())

    def test_markdown_to_html_quote(self):
        markdown = "> This is a quote\n> block"
        html_node = markdown_to_html_node(markdown)
        expected = HTMLNode("div", children=[HTMLNode("blockquote", children=[HTMLNode(None, value="This is a quote\nblock")])])
        self.assertEqual(html_node.to_html(), expected.to_html())

    def test_markdown_to_html_unordered_list(self):
        markdown = "* Item 1\n* Item 2\n- Item 3"
        html_node = markdown_to_html_node(markdown)
        expected = HTMLNode("div", children=[HTMLNode("ul", children=[
            HTMLNode("li", children=[HTMLNode(None, value="Item 1")]),
            HTMLNode("li", children=[HTMLNode(None, value="Item 2")]),
            HTMLNode("li", children=[HTMLNode(None, value="Item 3")])
        ])])
        self.assertEqual(html_node.to_html(), expected.to_html())

    def test_markdown_to_html_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2\n3. Item 3"
        html_node = markdown_to_html_node(markdown)
        expected = HTMLNode("div", children=[HTMLNode("ol", children=[
            HTMLNode("li", children=[HTMLNode(None, value="Item 1")]),
            HTMLNode("li", children=[HTMLNode(None, value="Item 2")]),
            HTMLNode("li", children=[HTMLNode(None, value="Item 3")])
        ])])
        self.assertEqual(html_node.to_html(), expected.to_html())

if __name__ == "__main__":
    unittest.main()