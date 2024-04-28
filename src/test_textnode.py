import unittest
from textnode import (
    TextNode,
    TextType
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        node2 = TextNode("This is a text node", TextType.BOLD,
                         'https://www.boot.dev')
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        node2 = TextNode("This is another text node", TextType.BOLD,
                         'https://www.boot.dev')
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        node3 = TextNode("This is a text node", TextType.ITALIC,
                         'https://www.boot.dev')
        self.assertNotEqual(node, node3)

    def test_eq_false3(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        node4 = TextNode("This is a text node", TextType.ITALIC,
                         'https://soliprem.github.io')
        self.assertNotEqual(node, node4)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        node2 = TextNode("This is a text node", TextType.BOLD,
                         'https://www.boot.dev')
        self.assertEqual(node.url, node2.url)

    def test_eq_url_false(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        node2 = TextNode("This is a text node", TextType.BOLD,
                         'https://soliprem.github.io')
        self.assertNotEqual(node.url, node2.url)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD,
                        'https://www.boot.dev')
        self.assertEqual(
            repr(node), "TextNode(This is a text node, bold, https://www.boot.dev)")


if __name__ == "__main__":
    unittest.main()
