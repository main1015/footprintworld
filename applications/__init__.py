# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from bottle import Bottle
from bottle import static_file

apps_home = Bottle()

@apps_home.route('/')
def home():
    return "Welcome!! '我日程'."



###############################################################################
#静态文件路由 ##################################################################
###############################################################################
@apps_home.route('/:path#(images|css|js|docs|fonts)/.+#')
def server_static(path):
    return static_file(path, root = 'static')

@apps_home.route('/:file#(favicon.ico)#')
def favicon(file):
    return static_file(file, root = '')



#@apps_home.route('/js/<path:path>')
#def server_static(path):
#    return static_file(path, root='static/js')
#
#
#@apps_home.route('/css/<path:path>')
#def server_static(path):
#    return static_file(path, root='static/css')
#
#
#@apps_home.route('/images/<path:path>')
#def server_static(path):
#    return static_file(path, root='static/images')

###############################################################################
