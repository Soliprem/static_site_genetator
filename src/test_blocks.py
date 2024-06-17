import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType


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

    # def test2(self):
    #     paragraph = """this is **bolded** paragraph
    #
    #     ```
    #     this is a code paragraph with *italic* text and stuff here
    #     this is the same paragraph on a new line
    #     ```
    #
    #     * this is a list
    #     * with items
    #     - more items
    #
    #     1. numbered list
    #     2. more numbers"""
    #
    #     blocks = ["this is **bolded** paragraph",
    #               "this is another paragraph with *italic* text and `code` here\nthis is the same paragraph on a new line",
    #               """* this is a list\n* with items"""
    #               ]
    #     self.assertequal(markdown_to_blocks(paragraph), blocks)
