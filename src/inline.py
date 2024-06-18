import re
from textnode import (
    TextNode,
    TextType,
)


def split_nodes_delimiter(old_nodes: list, delimiter, text_type):
    list = []
    for node in old_nodes:
        inside_delimiter = True
        if node.text_type != "text":
            list.append(node)
            continue
        new_text = node.text.split(delimiter)
        for i in new_text:
            inside_delimiter = not inside_delimiter
            if inside_delimiter:
                new_text_type = text_type
            else:
                new_text_type = TextType.TEXT
            list.append(TextNode(i, new_text_type))
    return list


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    list = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            list.append(old_node)
            continue
        old_text = old_node.text
        images = extract_markdown_images(old_text)
        for image_tup in images:
            old_text = old_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if old_text[0]:
                list.append(TextNode(old_text[0], TextType.TEXT))
            list.append(TextNode(image_tup[0], TextType.IMAGE, image_tup[1]))
            old_text = old_text[-1]
        if old_text:
            list.append(TextNode(old_text, TextType.TEXT))
    return list


def split_nodes_link(old_nodes):
    list = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            list.append(old_node)
            continue
        old_text = old_node.text
        links = extract_markdown_links(old_text)
        for link_tup in links:
            old_text = old_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if old_text[0]:
                list.append(TextNode(old_text[0], TextType.TEXT))
            list.append(TextNode(link_tup[0], TextType.LINK, link_tup[1]))
            old_text = old_text[-1]
        if old_text:
            list.append(TextNode(old_text, TextType.TEXT))
    return list


def text_to_textnode(text):
    old_nodes = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    codeblock = split_nodes_delimiter(italic, "`", TextType.CODE)
    images = split_nodes_image(codeblock)
    links = split_nodes_link(images)
    return links
