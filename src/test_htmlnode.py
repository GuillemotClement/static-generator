import unittest

from htmlnode import HTMLNode



class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("p", "Mon super text", ["p", "li"], {"class": "button"})
        html_node2 = HTMLNode("p", "Mon super text", ["p", "li"], {"class": "button"})
        self.assertEqual(html_node, html_node2)

    def test_eq_false(self):
        html_node = HTMLNode("p")
        html_node2 = HTMLNode("li")
        self.assertNotEqual(html_node, html_node2)

    # on test la methode __repr__
    def test_repr(self):
        html_node = HTMLNode("p", "Mon super texte", ["p", "li"], {"href": "http://link.com", "target": "_blank"})
        self.assertEqual(
            "HTMLNode(p, Mon super texte, ['p', 'li'], {'href': 'http://link.com', 'target': '_blank'})",repr(html_node)
        )


if __name__ == "__main__":
    unittest.main()