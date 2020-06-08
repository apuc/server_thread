import mimetypes
import os
from include.ServerThread import st
from http.server import HTTPServer, BaseHTTPRequestHandler  # Python 3


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        basePath = 'site/'
        try:
            if self.path in ("", "/"):
                filepath = "html/index.html"
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


severT = st.ServerThread()
severT.createServer(8181, SimpleHTTPRequestHandler)


def up():
    severT.start()
    print('starting server on port {}'.format(severT.server.server_port))


def down():
    severT.stop()
    print('stopping server on port {}'.format(severT.server.server_port))


if __name__ == "__main__":
    up()
    stopS = input('Остановить?')
    down()
