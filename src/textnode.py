class TextNode(object):
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self, OtherNode):
        if self.text == OtherNode.text and self.text_type == OtherNode.text_type and self.url == OtherNode.url:
            return True
        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
