#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains the necessary code to upload files to my S3 bucket """
from os import path, walk
import logging
import boto3  #  aws library
from botocore.exceptions import ClientError  #  aws library
from aws.progress import ProgressPercentage
from aws.utils.decorators import Logging, System


class S3Bucket:
    """ Class for handling my S3 bucket actions """

    def __init__(self, name: str, bucket: str, remote_folder: str,
                 local_folder=None, local_file=None) -> None:
        """ Default constructor """

        # Set local folder
        self._local_folder = local_folder

        # Set destination folder
        self._remote_folder = remote_folder

        # Set local file
        self._file = local_file

        # Set bucket name
        self._bucket = bucket

        # Initialize logger
        self._name = name

        # Configure logger
        self._logger = logging.getLogger(self._name)

    def _walk(self, root):
        """ Method to walk throught the given folder """
        for dirpath, dirnames, filenames in walk(root):
            # yield every filename to updload
            for filename in filenames:
                yield path.join(dirpath, filename)
            # call the method recursively for the subfolders
            for dirname in dirnames:
                self._walk(path.join(dirpath, dirname))

    def _upload(self, file_name, object_name=None):
        """ method to upload walked files to the S3 bucket """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = path.basename(file_name)

        if self._remote_folder:
            object_name = f'{self._remote_folder}/{object_name}'

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            _ = s3_client.upload_file(file_name, self._bucket, object_name,
                                      Callback=ProgressPercentage(file_name, self._name))
        except ClientError as error:
            self._logger.error(error)
            return False

        return True

    @Logging.trace_debug("Launching run ...")
    @System.execution_time
    def run(self):
        """ Public method for running defined actions """
        if self._local_folder:
            for item in self._walk(self._local_folder):
                self._logger.info("Uploading file %s ...", item)
                if self._upload(item):
                    self._logger.info("Ok")
                    continue

                self._logger.error("Fail")
            return True

        if self._file:
            self._logger.info("Uploading file %s ...", self._file)
            if self._upload(self._file):
                self._logger.info("Ok")
                return True

            self._logger.error("Fail")

        return False
