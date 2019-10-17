#! /usr/bin/python
# _*_ coding: utf-8 _*_
__author__ = 'Jeffery'
__date__ = '2019/2/5 19:40'


"""
1、formatter

%(levelno)s：打印日志级别的数值。

%(levelname)s：打印日志级别的名称。

%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]。

%(filename)s：打印当前执行程序名。

%(funcName)s：打印日志的当前函数。

%(lineno)d：打印日志的当前行号。

%(asctime)s：打印日志的时间。

%(thread)d：打印线程ID。

%(threadName)s：打印线程名称。

%(process)d：打印进程ID。

%(processName)s：打印线程名称。

%(module)s：打印模块名称。

%(message)s：打印日志信息。

2、handlers
    logging.StreamHandler, 日志输出到流，可以是 sys.stderr，sys.stdout 或者文件。
    logging.FileHandler,日志输出到文件。
    logging.handlers.BaseRotatingHandler；基本的日志回滚方式。
    logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚。
    logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件。
    logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets。
    logging.handlers.DatagramHandler；远程输出日志到UDP sockets。
    logging.handlers.SMTPHandler；远程输出日志到邮件地址。
    logging.handlers.SysLogHandler；日志输出到syslog。
    logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志。
    logging.handlers.MemoryHandler；日志输出到内存中的指定buffer。
    logging.handlers.HTTPHandler；通过”GET”或者”POST”远程输出到HTTP服务器。
    
3、levels
    logger.critical('critical err occur')
    logger.fatal('fatal error occur')
    logger.error('some error occur')
    logger.warning('Warning exists')
    logger.warn('Warning exists')
    logger.info('This is a log info')
    logger.debug('Debugging')
"""

import logging

# 'stream' or 'filename' or 'handlers' should not be specified together
logging.basicConfig(
                    filename='./log.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(funcName)s - %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    style='%',
                    level=logging.DEBUG
                    )
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

try:
    result = 10 / 0
except:
    logger.error('Faild to get result', exc_info=True)


# ------------------------------------------------------------------------------------
handler = logging.FileHandler('output.log', mode='a', encoding=None, delay=False)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                              datefmt='%Y/%m/%d %H:%M:%S',
                              style='%')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
handler.set_name('output-log')
logger.addHandler(handler)
# ------------------------------------------------------------------------------------


logger.log(50, 'logging critical test')
