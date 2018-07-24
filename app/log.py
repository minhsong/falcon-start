# -*- coding: utf-8 -*-

import sys
import logging


logging.basicConfig(level='DEBUG')
LOG = logging.getLogger('API')
LOG.propagate = False

INFO_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
DEBUG_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s [in %(pathname)s:%(lineno)d]'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'


stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT)
stream_handler.setFormatter(formatter)
LOG.addHandler(stream_handler)


def get_logger():
    return LOG
