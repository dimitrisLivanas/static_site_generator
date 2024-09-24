from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f'<{self.tag}{self.props_to_html()}/>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'