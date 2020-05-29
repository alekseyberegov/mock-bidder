from functools import partial
from http.server import ThreadingHTTPServer
from mockrtb.http.RtbHttpHandler import RtbHttpHandler


class RtbHttpEndpoint(object):
    def __init__(self, handler_class=RtbHttpHandler):
        self.handler_class = handler_class

    def run(self, port=9000, base_url='http://localhost'):
        server_address = ('', port)
        handler = partial(self.handler_class, base_url)
        httpd = ThreadingHTTPServer(server_address, handler)
        httpd.serve_forever()

