import unittest
from textnode import TextNode
from markdown_parser import (split_nodes_delimiter,
                             text_type_text,
                             text_type_bold,
                             text_type_italic,
                             text_type_code,
                             text_type_image,
                             text_type_link,
                             split_nodes_image,
                             split_nodes_link)

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

    def test_split_nodes_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type_text)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", text_type_text),
            TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text with no images.", text_type_text)
        new_nodes = split_nodes_image([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is text with no links.", text_type_text)
        new_nodes = split_nodes_link([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()