import io
import sys
import traceback
import urllib
from http.server import SimpleHTTPRequestHandler
from mockrtb.bidder.Bidder import Bidder
from mockrtb.serialize.ValidationError import ValidationError


class RtbHttpHandler(SimpleHTTPRequestHandler):
    def __init__(self, base_url,  *args, **kwargs):
        self.bidder = Bidder(base_url)
        super().__init__(*args, **kwargs)

    def send_unsupported(self, capability):
        output = io.BytesIO()
        self.send_response(400)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        resp_body = '{"error": "%s is not supported"}' % capability
        output.write(bytes(resp_body, 'utf-8'))
        output.seek(0)
        self.wfile.write(output.read())

    @staticmethod
    def create_error_response():
        exc_type, exc_value, exc_traceback = sys.exc_info()
        res: str = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
        res = '{"error": "malformed request", "stacktrace" : "%s"}' % urllib.parse.quote(res)
        return res

    def do_GET(self):
        self.send_unsupported('GET')

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length).decode('utf-8')

        try:
            res = self.bidder.process_request(content)
            code = 200
        except (ValidationError, ValueError):
            res = self.create_error_response()
            code = 400

        self.send_response(code)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(bytes(res, 'utf-8'))
