from urllib import parse

import requests
from bottle import Bottle, request as bottle_request

from .utils import HtmlModifier, TMAppender


class ProxyServer:
    def __init__(self, to, port):
        self._base_uri = to if to.endswith("/") else to + "/"
        self._port = port
        self._server_uri = f"http://localhost:{self._port}/"
        self._app = Bottle()
        self._init_route()

    def _init_route(self):
        self._app.route("/<uri:re:.+>", callback=self._proxy)
        self._app.route("/", callback=self._proxy)

    def _proxy(self, uri="/"):
        response = self._get_response(uri)
        if "text/html" in response.headers["Content-Type"]:
            return self._get_modified_html(response.text)
        else:
            return response.content

    def _get_response(self, uri):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'
        }
        full_uri = parse.urljoin(self._base_uri, uri)
        return requests.get(full_uri, headers=headers, params=dict(bottle_request.GET))

    def _get_modified_html(self, raw_html):
        html_modifier = HtmlModifier(raw_html)
        html_modifier.all_a_href_to_relative(self._base_uri)
        html_modifier.all_links_to_absolute(self._base_uri)
        html_modifier.modify_all_text(TMAppender(special_len=6))
        return html_modifier.get_html()

    def start(self):
        self._app.run(port=self._port)
