class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        # represente element HTML
        self.tag = tag
        # represente la valeur de l'element
        self.value = value
        # list d'objet HTMLNode qui represente les enfants
        self.children = children
        # dictionnaire de cle valeur qui represente les attributs HTML
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented yet")

    def props_to_html(self):
        str_props = None
        length_props = len(self.props)
        i = 0
        for key in self.props:
            str_props += f"{key}={self.props[key]}"
            if i < length_props:
                str_props += " "
            i += 1
        return str_props

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.tag == other.tag and \
                self.value == other.value and \
                self.children == other.children and \
                self.props == other.props
        else:
            return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
