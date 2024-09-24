import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

if __name__ == "__main__":
    unittest.main()