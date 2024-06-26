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
    new_markdown = re.sub("\n\n\n*", "\n\n", new_markdown)
    return new_markdown.split("\n\n")


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
    new_block = block[3:-3].split("\n", 1)
    node = LeafNode("code", new_block[1], {"data-lang": new_block[0]})
    return ParentNode("pre", node)


def heading_to_html(block):
    if re.findall("^#{1} ", block):
        header = "h1"
        index = 1
    if re.findall("^#{2} ", block):
        header = "h2"
        index = 2
    if re.findall("^#{3} ", block):
        header = "h3"
        index = 3
    if re.findall("^#{4} ", block):
        header = "h4"
        index = 4
    if re.findall("^#{5} ", block):
        header = "h5"
        index = 5
    if re.findall("^#{6} ", block):
        header = "h6"
        index = 6
    text_nodes = text_to_textnode(block[index:])
    html_nodes = list(map(text_node_to_html_node, text_nodes))
    return ParentNode(header, html_nodes)


def quote_to_html(block):
    split_block = block.split("\n")
    stripped_split_block = list(map(lambda x: x[1:], split_block))
    stripped_split_block = "\n".join(stripped_split_block)
    return ParentNode("blockquote", list(map(lambda x: text_node_to_html_node(x), text_to_textnode(stripped_split_block))))


def paragraph_to_html(block):
    return ParentNode("p", list(map(lambda x: text_node_to_html_node(x), text_to_textnode(block))))


def listify(block, ordered):
    if ordered:
        index = 3
    else:
        index = 2
    new_block = block.split("\n")
    stripped_new_block = list(map(lambda x: x[index:], new_block))
    text_nodes = list(map(text_to_textnode, stripped_new_block))
    html_nodes = list(
        map(lambda x: [text_node_to_html_node(y) for y in x], text_nodes))
    children = list(map(lambda x: ParentNode("li", x), html_nodes))
    return children


def unordered_list_to_html(block):
    return ParentNode("ul", listify(block, False))


def ordered_list_to_html(block):
    return ParentNode("ol", listify(block, True))


def markdown_to_html_node(markdown):
    while markdown[:1] == "\n":
        markdown = markdown[1:]
    while markdown[-1:] == "\n":
        markdown = markdown[:-1]
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
    return ParentNode("div", children)
