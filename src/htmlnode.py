class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        if self.value is not None:
            return self.value
        children_html = ''.join(child.to_html() for child in self.children)
        if self.tag is None:
            return children_html
        return f'<{self.tag}>{children_html}</{self.tag}>'
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.children == other.children

    def props_to_html(self):
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'