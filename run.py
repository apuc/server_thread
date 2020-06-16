import mimetypes
import os
import socketserver

from include.ServerThread import st, stDTO, stPool, stHandlerDTO, stRequestHandler, stDesign
from http.server import HTTPServer, BaseHTTPRequestHandler  # Python 3





def up():
    severT.start()
    severT2.start()
    print('starting server on port {}'.format(severT.server.server_port))
    print('starting server on port {}'.format(severT2.server.server_port))


def down():
    severT.stop()
    severT2.stop()
    print('stopping server on port {}'.format(severT.server.server_port))
    print('stopping server on port {}'.format(severT2.server.server_port))


if __name__ == "__main__":
    severT = st.ServerThread()
    severT2 = st.ServerThread()

    severT.createServer(8282, stRequestHandler.RequestHandler)
    severT2.createServer(8383, stRequestHandler.RequestHandler)

    severT.server.handlerDto = stHandlerDTO.handlerDTO(rootPath='/var/www/')
    severT2.server.handlerDto = stHandlerDTO.handlerDTO(rootPath='/var/www2/')

    dto = stDTO.Messenger(id=severT.getName(), thread=severT)
    dto2 = stDTO.Messenger(id=severT2.getName(), thread=severT2)

    pool = stPool.Pool()

    pool.add(dto)
    pool.add(dto2)

    up()
    stopS = input('Остановить?')
    down()
