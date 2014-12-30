#!/usr/bin/env python
import logging

import tornado.ioloop
import tornado.options
from tornado.options import options, define

from application import Application


define('target', default="development", help="development or production", type=str)
define('port', default=8888, help="port", type=int)


def main():
    tornado.options.parse_command_line(final=False)  # Do this to get the target option first
    tornado.options.parse_config_file("settings/{target}.py".format(target=options.target), final=False)
    tornado.options.parse_command_line()  # then override with the rest of the manual settings
    app = Application()
    app.listen(options.port)

    logging.info("Booting {target} mode".format(target=options.target))
    logging.info("Server started on port {port}".format(port=options.port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
