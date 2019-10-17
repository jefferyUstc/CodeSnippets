#! /usr/bin/python
# _*_ coding: utf-8 _*_
__author__ = 'Jeffery'
__date__ = '2019/2/7 20:08'

import logging
# import core

# logger = logging.getLogger('main')
logger = logging.getLogger('main')
logger.setLevel(level=logging.DEBUG)

print(logger.getEffectiveLevel())
print(logger.isEnabledFor(20))
print(logger.disabled)
logging.disable(20)
print(logger.isEnabledFor(20))
print(logger.isEnabledFor(30))
# logger.propagate = True
# Handler
# handler = logging.FileHandler('result.log')
# handler.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
#
# logger.info('Main Info')
# logger.debug('Main Debug')
# logger.error('Main Error')
# core.run()

