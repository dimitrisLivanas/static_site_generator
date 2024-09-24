import unittest
from textnode import TextNode
from conversion import text_node_to_html_node
from leafnode import LeafNode

class TestConversion(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold_node(self):
        text_node = TextNode("Bold text", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_italic_node(self):
        text_node = TextNode("Italic text", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_code_node(self):
        text_node = TextNode("Code text", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_link_node(self):
        text_node = TextNode("Click me!", "link", "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_image_node(self):
        text_node = TextNode("Image alt text", "image", "https://www.example.com/image.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.png" alt="Image alt text"/>')

    def test_unknown_text_type(self):
        text_node = TextNode("Unknown text", "unknown")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()