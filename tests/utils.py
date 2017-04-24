from bs4 import BeautifulSoup


def get_formatted_html(html):
    return str(BeautifulSoup(html, "html5lib")).strip()
