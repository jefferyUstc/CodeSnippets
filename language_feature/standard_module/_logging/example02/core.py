#! /usr/bin/python
# _*_ coding: utf-8 _*_
__author__ = 'Jeffery'
__date__ = '2019/2/7 20:09'

import logging

logger = logging.getLogger('main.core')


def run():
    logger.info('Core Info')
    logger.debug('Core Debug')
    logger.error('Core Error')


if __name__ == '__main__':
    run()
