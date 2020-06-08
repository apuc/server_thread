from collections import namedtuple


class handlerDTO(namedtuple('handlerDTO', ['rootPath'])):
    __slots__ = ()
    def __new__(cls, rootPath='/var/www/html/'):
        return super(handlerDTO, cls).__new__(cls, rootPath)