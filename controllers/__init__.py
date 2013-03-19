# -*- coding: utf-8 -*-
from applications import apps_home
from beaker.middleware import SessionMiddleware
from bottle import Bottle
from config import SESSION_OPTS

__author__ = 'Administrator'

#路由配置
DEFAULT_MODULES = (
    (apps_home,"/"),
)




def create_app(config=None, modules=None,session = False):
    if modules is None:
        modules = DEFAULT_MODULES

    app = Bottle()

    # 插件安装
    canvas = CanvasPlugin()
    template = TemplatePlugin()
    #    hooks = HooksPlugin()
    #    hooks.add('before_request',__)
    plugins = [canvas,template]#,hooks
    #    jinja2_template =
    # 添加子模块
    for route in modules:
        if len(route) == 2:
            for plugin in plugins:
                route[0].install(plugin)
            if route[1]== '' or route[1]== '/':
                app.merge(route[0])
            else:
                app.mount(*route)
        else:
            print u'路由格式错误！！'
#            raise HTTPError(500, "Database Error")

    #忽略尾部的反斜杠
    app = StripPathMiddleware(app)

    #添加session功能
    if session:
        app = SessionMiddleware(app, SESSION_OPTS)
    return app

#app = SessionMiddleware(bottle.app(), session_opts)

class StripPathMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.app(e,h)