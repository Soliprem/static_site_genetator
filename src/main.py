from textnode import (
    TextNode,
    TextType,
    text_node_to_html_node
)
from htmlnode import (
    HTMLNode, 
    LeafNode,
    ParentNode)


def main():
    first_node = TextNode('this is a text node', TextType.BOLD,
                          'https://www.boot.dev')
    second_node = TextNode('this is an image', TextType.IMAGE, 'https://filelink.com')
    htmlnode = HTMLNode('a', 'value')
    print(first_node)
    print(first_node.text_type)
    print(htmlnode)
    print(text_node_to_html_node(first_node))
    print(text_node_to_html_node(second_node))


main()
