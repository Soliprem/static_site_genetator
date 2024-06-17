class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            pass
        return_string = ""
        for key in self.props:
            return_string += f' {key}="{self.props[key]}"'
        return return_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

    def __eq__(self, other):
        return (self.tag == other.tag
                and self.value == other.value
                and self.props == other.props
                and self.children == other.children)

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        if self.children:
            raise ValueError('LeafNodes may not have children')
        if self.value is None:
            raise ValueError('LeafNodes need to have values')

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self, i=-1):
        if self.tag is None:
            raise ValueError('ParentNodes need to have a tag')
        if self.children is None:
            raise ValueError('ParentNodes need to have children')
        i += 1
        if i >= (len(self.children)):
            return ''
        if i == 0:
            return f'<{self.tag}>{self.children[i].to_html()}{self.to_html(i)}</{self.tag}>'
        return f'{self.children[i].to_html()}{self.to_html(i)}'
