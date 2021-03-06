# -*- coding: utf-8 -*-
import tornado.ioloop
from tornado.web import Application, RequestHandler
from tornado.options import define, options

class MainHandler(RequestHandler):
    def get(self):
        self.write('Hello, world!')


def main():
    define("host", default="127.0.0.1", help="Host IP")
    define("port", default=8080, help="Port")
    tornado.options.parse_command_line()

    application = Application([(r"/", MainHandler),])

    application.listen(options.port, options.host)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
