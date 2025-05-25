from textnode import TextNode, TextType


def main():
    # on fait reference au valeur stocker dans l'enum
    textNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textNode.__repr__())

if __name__ == "__main__":
    main()
