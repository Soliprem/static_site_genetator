from enum import Enum


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
        raise Exception('Invalid Type')


class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6
