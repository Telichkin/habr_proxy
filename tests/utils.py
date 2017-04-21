from bs4 import BeautifulSoup


def get_formatted_html(html):
    return BeautifulSoup(html, "html.parser").prettify().strip()
