#! /usr/bin/python
# _*_ coding: utf-8 _*_
__author__ = 'Jeffery'
__date__ = '2019/2/7 20:14'

import logging
import yaml
import logging.config
import os
import core


def setup_logging(default_path='config.yaml', default_level=logging.INFO):
    if os.path.exists(default_path):
        with open(default_path, 'r', encoding='utf-8') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def log():
    logging.debug('Start')
    logging.info('Exec')
    logging.info('Finished')


if __name__ == '__main__':
    yaml_path = 'config.yaml'
    setup_logging(yaml_path)
    log()
    core.run()
