import pytest

from .utils import get_formatted_html
from .test_data import html_raw_and_expected_a_href, html_raw_and_expected_text, html_raw_and_expected_links
from habr_proxy.utils import HtmlModifier


class FakeContentModifier:
    def get_modified_text(self, raw_text):
        if raw_text != "\n":
            return "1"
        else:
            return ""


class HtmlModifierTest:
    RESOURCE_ROOT_URI = "https://habrahabr.ru/"

    @pytest.mark.parametrize(["html", "expected_html"], html_raw_and_expected_a_href)
    def test_should_replace_all_a_href_to_relative(self, html, expected_html):
        html_modifier = HtmlModifier(html)
        html_modifier.all_a_href_to_relative(self.RESOURCE_ROOT_URI)

        assert get_formatted_html(expected_html) == get_formatted_html(html_modifier.get_html())

    @pytest.mark.parametrize(["html", "expected_html"], html_raw_and_expected_links)
    def test_should_replace_all_links_to_absolute(self, html, expected_html):
        html_modifier = HtmlModifier(html)
        html_modifier.all_links_to_absolute(self.RESOURCE_ROOT_URI)

        assert get_formatted_html(expected_html) == get_formatted_html(html_modifier.get_html())

    @pytest.mark.parametrize(["html", "expected_html"], html_raw_and_expected_text)
    def test_should_modify_all_text(self, html, expected_html):
        html_modifier = HtmlModifier(html)
        html_modifier.modify_all_text(FakeContentModifier())

        assert get_formatted_html(expected_html) == get_formatted_html(html_modifier.get_html())

