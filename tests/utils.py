from bs4 import BeautifulSoup


def get_formatted_html(html):
    return BeautifulSoup(html, "html5lib").prettify().strip()
