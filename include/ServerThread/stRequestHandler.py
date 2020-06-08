import mimetypes
import os
from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        basePath = self.server.handlerDto.rootPath
        try:
            if self.path in ("", "/"):
                filepath = "index.html"
            else:
                filepath = self.path.lstrip("/")

            finalPath = basePath + filepath
            f = open(os.path.join('.', finalPath), "rb")

        except IOError:
            self.send_error(404, 'File Not Found: %s ' % finalPath)

        else:
            self.send_response(200)

            # this part handles the mimetypes for you.
            mimetype, _ = mimetypes.guess_type(finalPath)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            for s in f:
                self.wfile.write(s)
