import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('a', 'this is a test')
        node1 = HTMLNode('a', 'this is a test')
        self.assertEqual(node, node1)

    def test_props_to_html(self):
        node = HTMLNode('a', 'this is a test', None, {
                        "href": "https://www.google.com", "target": "_blank"})
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_repr(self):
        node = HTMLNode('a', 'this is a test', ['a', 'b', 'c'], {
            "href": "https://www.google.com", "target": "_blank"})
        result = "HTMLNode(a, this is a test, ['a', 'b', 'c'], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), result)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()
