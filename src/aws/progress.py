#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains the code to handle the progress percentage of an upload """

import os
import sys
import threading
import logging


class ProgressPercentage(object):
    """ Class to handle callback to the s3 upload_file function """

    def __init__(self, filename, logger_name):
        """ Default constructor """

        # Set the filename
        self._filename = filename

        # Get logger
        self._logger = logging.getLogger(logger_name)

        # Get the filename size in bytes
        self._size = float(os.path.getsize(filename))

        # Initialize transferred bytes
        self._seen_so_far = 0

        # Set lock
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        """  """
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()
