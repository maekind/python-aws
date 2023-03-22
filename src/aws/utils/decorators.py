#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains decorators usefull for the project """

import logging
import functools
import time

__author__ = "Marco Espinosa"
__email__ = "marco@marcoespinosa.es"
__date__ = "22/03/2023"
__version__ = "1.0"
__development__ = True


class Logging:
    """ This class provides with usefull decorators for logging purpouses """

    @staticmethod
    def trace_info(message):
        """ trace logging info decorator """
        def decorator(func):
            """ decorator for function """
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                """ wrapper for the decorator """
                logger = logging.getLogger(args[0]._name)
                logger.info("%s", message)
                res = func(*args, **kwargs)
                logger.info("ok")
                return res
            return wrapper
        return decorator

    @staticmethod
    def trace_debug(message):
        """ trace logging debug decorator """
        def decorator(func):
            """ decorator for function """
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                """ wrapper for the decorator """
                logger = logging.getLogger(args[0]._name)
                logger.debug("%s", message)
                res = func(*args, **kwargs)
                logger.debug("ok")
                return res
            return wrapper
        return decorator


class System:
    """ This class provides with usefull decorators for system purpouses """

    @staticmethod
    def execution_time(func):
        """ calculates function time execution """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """ decorator wrapper """
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()

            logger = logging.getLogger(args[0]._name)
            logger.debug(
                    'Method Name "%s", Execution Time: %s s', 
                    func.__name__, end_time - start_time)

            return res
        return wrapper
