import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def markdown_to_blocks(markdown):
    new_markdown = markdown.split("\n")
    new_markdown = list(map(lambda x: x.strip(), new_markdown))
    new_markdown = ('\n').join(new_markdown)
    return new_markdown.split("\n\n")


markdown_to_blocks("""This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items""")


def block_to_block_type(block):
    split_block = block.split("\n")
    firsts = list(map(lambda x: x[0], split_block))
    seconds = list(map(lambda x: x[1], split_block))
    thirds = list(map(lambda x: x[2], split_block))
    if block[-3:] == "```" and block[:3] == "```":
        return BlockType.CODE
    if re.match("^#{1,6} ", block):
        return BlockType.HEADING
    if all(element == ">" for element in firsts):
        return BlockType.QUOTE
    if all(element == "-" or element == "*" for element in firsts) and all(element == " " for element in seconds):
        return BlockType.UNORDERED_LIST
    if all(re.match("\\d", element) for element in firsts) and all(element == "." for element in seconds) and all(element == " " for element in thirds):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
