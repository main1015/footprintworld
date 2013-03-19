# -*- coding: utf-8 -*-
from util.address import get_ip_address

__author__ = 'Administrator'

IS_DEBUG = True
IS_SESSION = False
IS_RELOADER = True


HOST = get_ip_address('eth0')
PORT = 8080



#session配置
SESSION_OPTS = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}