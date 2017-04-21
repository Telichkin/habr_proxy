from habr_proxy.proxy_server import ProxyServer


if __name__ == '__main__':
    p = ProxyServer(to="https://habrahabr.ru/", port=8232)
    p.start()
