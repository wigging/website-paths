import webbrowser
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


def run_server():
    """
    Run a local server and open a browser to view the website.
    """

    server_address = ('localhost', 9000)
    handler = partial(SimpleHTTPRequestHandler, directory='docs')
    httpd = HTTPServer(server_address, handler)

    print('Serving at http://localhost:9000')
    webbrowser.open('http://localhost:9000')

    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
