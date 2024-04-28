from textnode import (
    TextNode,
    TextType
)


def main():
    first_node = TextNode('this is a text node', TextType.BOLD,
                          'https://www.boot.dev')
    print(first_node)


main()
