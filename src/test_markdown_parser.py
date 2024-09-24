import unittest
from textnode import TextNode
from markdown_parser import split_nodes_delimiter, text_type_text, text_type_bold, text_type_italic, text_type_code

class TestMarkdownParser(unittest.TestCase):
    def test_split_text_with_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_text_with_bold(self):
        node = TextNode("This is **bold** text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_text_with_italic(self):
        node = TextNode("This is *italic* text", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is `unmatched code block", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", text_type_code)

if __name__ == "__main__":
    unittest.main()