import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node, listify
from htmlnode import ParentNode, LeafNode


class TestSplits(unittest.TestCase):
    def test1(self):
        paragraph = """this is **bolded** paragraph\n\nthis is another paragraph with *italic* text and `code` here\nthis is the same paragraph on a new line

* this is a list
* with items"""
        blocks = ["this is **bolded** paragraph",
                  "this is another paragraph with *italic* text and `code` here\nthis is the same paragraph on a new line",
                  """* this is a list\n* with items"""
                  ]
        self.assertEqual(markdown_to_blocks(paragraph), blocks)

    def test2(self):
        paragraph = "```code code code\ncodeoksjldckj```"
        self.assertEqual(block_to_block_type(paragraph), BlockType.CODE)

    def test3(self):
        paragraph = "* this is a bulleted list\n* more bullets\n- more bullets"
        self.assertEqual(block_to_block_type(
            paragraph), BlockType.UNORDERED_LIST)

    def test4(self):
        paragraph = "1. this is a bulleted list\n2. more bullets\n3. more bullets"
        self.assertEqual(block_to_block_type(
            paragraph), BlockType.ORDERED_LIST)

    def test5(self):
        paragraph = "1.this is a bulleted list\n2. more bullets\n3. more bullets"
        self.assertEqual(block_to_block_type(
            paragraph), BlockType.PARAGRAPH)

    def test6(self):
        #         paragraph = """
        #
        #
        # # this is a header paragraph
        #
        # ```
        # this is a code paragraph with
        #     indented text and stuff here
        # this is the same paragraph on a new line
        # ```
        #
        # ## pay attention!
        #
        #                    * this is a list
        # * with items. Even a [link](example.org) and a ![picture](~/imgs/puicsd)
        # - more items
        #
        # 1. numbered list
        # 2. more numbers
        #
        # a small ```dissertation``` about the *meaning* of **life**
        #
        # > and finally a quote
        # > block, to tie things off
        #
        #
        # """
        #
        # my_answer = markdown_to_html_node(paragraph)
        # print(my_answer.to_html())
        # answer = ParentNode("<div>", [LeafNode("<h1>", "this is a header paragraph"), ParentNode("<pre>", LeafNode("<code>", "\nthis is a code paragraph with\n\tindented text and stuff here\nthis is the same paragraph on a new line"), LeafNode("<h2>", "pay attention!"), ParentNode("<ul>", [ParentNode("<li>", [LeafNode()])])))
        print(listify("""- 1
- 2, **bold**
- 3, *italic*
- 4""", True))
