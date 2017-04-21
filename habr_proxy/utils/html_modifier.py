from urllib import parse

from bs4 import BeautifulSoup


class HtmlModifier:
    def __init__(self, html_string):
        self._modified_html = html_string

    @property
    def _soup(self):
        return BeautifulSoup(self._modified_html, "html5lib")

    def get_html(self):
        return self._soup.prettify()

    def all_a_href_to_relative(self, from_base_uri):
        soup = self._soup
        for a_tag in soup.find_all("a"):
            if a_tag.get("href", None) is not None:
                a_tag["href"] = a_tag["href"].replace(from_base_uri, "/")
                a_tag["href"] = a_tag["href"].replace(from_base_uri.strip("/"), "/")
        self._modified_html = str(soup)

    def modify_all_text(self, text_modifier):
        soup = self._soup
        for element in soup.find_all():
            if element.name != "script":
                self._modify_text_inside_element(element, text_modifier)
        self._modified_html = str(soup)

    @staticmethod
    def _modify_text_inside_element(element, text_modifier):
        for text in list(element.strings):
            new_text = text_modifier.get_modified_text(text)
            text.replaceWith(new_text)

    def all_links_to_absolute(self, base_resource_uri):
        soup = self._soup
        for link in soup.find_all("link"):
            link["href"] = parse.urljoin(base_resource_uri, link["href"])
        self._modified_html = str(soup)
