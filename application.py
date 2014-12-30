import logging

from tornado.options import options, define
import tornado.web


define('debug', default=False, help="debug mode", type=bool)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = []
        settings = {
            'debug': options.debug,
        }
        tornado.web.Application.__init__(self, handlers, **settings)
