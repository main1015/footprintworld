# -*- coding: utf-8 -*-
from function import log

__author__ = 'Administrator'


log.set_logger( filename = 'mylog.log', mode='a',level='ERROR:INFO')

log.debug('hello, world')
log.info('hello, world')
log.warning('hello, world')
log.error('hello, world')
log.critical('hello, world')
