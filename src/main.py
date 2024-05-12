from textnode import (
    TextNode,
    TextType
)
from htmlnode import HTMLNode


def main():
    first_node = TextNode('this is a text node', TextType.BOLD,
                          'https://www.boot.dev')
    htmlnode = HTMLNode('a', 'value')
    print(first_node)
    print(htmlnode)


main()
