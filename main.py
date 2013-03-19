# -*- coding: utf-8 -*-
import os
from bottle import run
from config import IS_SESSION, IS_RELOADER, IS_DEBUG, HOST, PORT
from controllers import create_app

__author__ = 'Administrator'



if __name__ == '__main__':

    app = create_app(session=IS_SESSION)
    #bottle.TEMPLATE_PATH=['/web2py/applications/myapp/views/demo/']
    # print '%s:%d' % (HOST,PORT)
    run(app, host=HOST, port=PORT, reloader=IS_RELOADER,debug=IS_DEBUG)
else:
    # Mod WSGI launch
    os.chdir(os.path.dirname(__file__))
    application = create_app(session=IS_SESSION)
