from enum import Enum
from htmlnode import LeafNode, ParentNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = self.__assign_type__(text_type)
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __assign_type__(self, text_type):
        if text_type == TextType.TEXT:
            return "text"
        if text_type == TextType.BOLD:
            return 'bold'
        if text_type == TextType.ITALIC:
            return 'italic'
        if text_type == TextType.CODE:
            return 'code'
        if text_type == TextType.LINK:
            return 'link'
        if text_type == TextType.IMAGE:
            return 'image'
        if text_type == TextType.BOLDITALIC:
            return 'bold_italic'
        if text_type == TextType.CODEBOLD:
            return 'code_bold'
        if text_type == TextType.CODEITALIC:
            return 'code_italic'
        if text_type == TextType.CODEITALICBOLD:
            return 'code_italic_bold'
        raise Exception('Invalid Type')


class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    BOLDITALIC = BOLD + ITALIC
    CODEBOLD = CODE + BOLD
    CODEITALIC = CODE + ITALIC
    LINK = 8
    CODEITALICBOLD = CODE + ITALIC + BOLD
    IMAGE = 10


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case 'text':
            return LeafNode(None, text_node.text)
        case 'bold':
            return LeafNode('b', text_node.text)
        case 'italic':
            return LeafNode('i', text_node.text)
        case "bold_italic":
            return ParentNode('b', LeafNode('i', text_node.text))
        case "code_bold":
            return ParentNode('b', LeafNode('code', text_node.text))
        case "code_italic":
            return ParentNode('i', LeafNode('code', text_node.text))
        case "code_italic_bold":
            return ParentNode('i', [ParentNode('b', LeafNode('code', text_node.text))])
        case 'code':
            return LeafNode('code', text_node.text)
        case 'link':
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case 'image':
            return LeafNode('img', "", {'src': text_node.url, 'alt': text_node.text})
    raise Exception(f'Invalid Type:{text_node.text_type}')
