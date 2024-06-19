import unittest
from textnode import (
    TextNode,
    TextType
)
from inline import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnode
)


class TestInlineSeparator(unittest.TestCase):
    def test1(self):
        node = TextNode(
            "This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, result)

    def test2(self):
        node = TextNode(
            "This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode(
            "This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, result)

    def test3(self):
        node = TextNode(
            "This is text with an *italic block* word", TextType.TEXT)
        node2 = TextNode(
            "This is text with an *italic block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "*", TextType.ITALIC)
        result = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, result)

    def test4(self):
        node = TextNode(
            "This is text with a **bold block** word", TextType.TEXT)
        node2 = TextNode(
            "This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, result)

    def test5(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        images = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                  ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(images, extract_markdown_images(text))

    def test6(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links = [("link", "https://www.example.com"),
                 ("another", "https://www.example.com/another")]
        self.assertEqual(links, extract_markdown_links(text))

    def test7(self):
        text = "This is **text** with an *italic* word and a `code block`. Also, a ***super*** and an ***```ubersuper```*** combination and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(". Also, a ", TextType.TEXT),
            TextNode("super", TextType.BOLDITALIC),
            TextNode(" and an ", TextType.TEXT),
            TextNode("ubersuper", TextType.CODEITALICBOLD),
            TextNode(" combination and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.maxDiff = None
        self.assertEqual(text_to_textnode(text), nodes)

    def test8(self):
        text = """This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"""
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.maxDiff = None
        self.assertEqual(text_to_textnode(text), nodes)
