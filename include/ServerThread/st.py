import threading
from http.server import HTTPServer


class ServerThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ServerThread, self).__init__(*args, **kwargs)
        self.deamon = True
        self._stop_event = threading.Event()

    def stop(self):
        self.server.shutdown()
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def createServer(self, port, handler):
        self.server = HTTPServer(('0.0.0.0', port), handler)

    def run(self):
        self.server.serve_forever()