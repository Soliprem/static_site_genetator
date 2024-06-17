import unittest
from textnode import (
    TextNode,
    TextType
)


from inline import (
    split_nodes_image,
    split_nodes_link
)


class TestSplits(unittest.TestCase):
    def test1(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        results = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(new_nodes, results)

    def test2(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        results = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ]
        self.assertEqual(new_nodes, results)

    def test3(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "[Demonio](Demonio) = divinità interemedia che muore e rinasce costantemente (non immortale e non mortale)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node, node2])
        results = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
            TextNode("Demonio", TextType.LINK, "Demonio"),
            TextNode(
                " = divinità interemedia che muore e rinasce costantemente (non immortale e non mortale)", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, results)

    def test4(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png), then the text continues",
            TextType.TEXT,
        )
        node2 = TextNode(
            "[Demonio](Demonio) = divinità interemedia che muore e rinasce costantemente (non immortale e non mortale)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node, node2])
        results = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK,
                     "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
            TextNode(
                ", then the text continues", TextType.TEXT
            ),
            TextNode("Demonio", TextType.LINK, "Demonio"),
            TextNode(
                " = divinità interemedia che muore e rinasce costantemente (non immortale e non mortale)", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, results)
