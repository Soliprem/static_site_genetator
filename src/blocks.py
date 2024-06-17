import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import (
    TextNode,
    text_node_to_html_node,
    TextType
)
from inline import text_to_textnode
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
    new_markdown = list(map(lambda x: x.rstrip(), new_markdown))
    new_markdown = ('\n').join(new_markdown)
    return new_markdown.split("\n\n")


markdown_to_blocks("""This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items""")


def block_to_block_type(block):
    split_block = block.split("\n")
    stripped_split_block = list(map(lambda x: x.strip(), split_block))
    firsts = list(map(lambda x: x[0], stripped_split_block))
    seconds = list(map(lambda x: x[1], stripped_split_block))
    thirds = list(map(lambda x: x[2], stripped_split_block))
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


def code_block_to_html(block):
    node = LeafNode("<code>", block)
    return ParentNode("<pre>", node)


def heading_to_html(block):
    match block:
        case re.match("^#{1} ", block):
            header = "h1"
        case re.match("^#{2} ", block):
            header = "h2"
        case re.match("^#{3} ", block):
            header = "h3"
        case re.match("^#{4} ", block):
            header = "h4"
        case re.match("^#{5} ", block):
            header = "h5"
        case re.match("^#{6} ", block):
            header = "h6"
    return LeafNode(header, block)


def quote_to_html(block):
    return ParentNode("<blockquote>", text_node_to_html_node(TextNode(block, TextType.TEXT)))


def paragraph_to_html(block):
    return ParentNode("<p>", text_node_to_html_node(TextNode(block, TextType.TEXT)))


def listify(block):
    new_block = block.split("\n")
    children = list(map(lambda x: ParentNode(
        "<li>", text_node_to_html_node(TextNode(x, TextType.TEXT))), new_block))
    return children


def unordered_list_to_html(block):
    return ParentNode("<ul>", listify(block))


def ordered_list_to_html(block):
    return ParentNode("<il>", listify(block))


def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.ORDERED_LIST:
                children.append(ordered_list_to_html(block))
            case BlockType.UNORDERED_LIST:
                children.append(unordered_list_to_html(block))
            case BlockType.PARAGRAPH:
                children.append(paragraph_to_html(block))
            case BlockType.QUOTE:
                children.append(quote_to_html(block))
            case BlockType.HEADING:
                children.append(heading_to_html(block))
            case BlockType.CODE:
                children.append(code_block_to_html(block))
    return ParentNode("<div>", children)
