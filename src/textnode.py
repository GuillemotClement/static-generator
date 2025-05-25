from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text # content from the node
        self.text_type = text_type # type of the node => member of enum TextType
        self.url = url # url of image or link. None autrement

    # methode utiliser dans les tests
    # indique a Python comment comparer les deux objets.
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.text == other.text and \
                    self.text_type == other.text_type and \
                    self.url == other.url
        else:
            return False

    # methode pour creer une representation de TextNode
    # ameliore l'affichage d'information
    # .value permet d'acceder a la valeur definis dans l'enum
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"