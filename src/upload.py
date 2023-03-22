#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file contains the main program for uploading files to my S3 bucket at the aws """
import sys
import logging
import argparse
from aws.utils.logger import Logger
from aws.aws_wrapper import S3Bucket

__application_name__ = "AWS S3 uploader"


def configure_logger(verbose, console):  # pragma: no cover
    """ Method for configuring default logging options """
    log_level = logging.INFO if not verbose else logging.DEBUG
    log_file = f'{__application_name__.replace(" ", "").lower()}.log'

    return Logger.get_logger(__application_name__,
                             log_level,
                             log_file,
                             console)


def get_arguments():  # pragma: no cover
    """ Method to retrieve application arguments """
    # Configure arguments
    parser = argparse.ArgumentParser(description=__application_name__)
    parser.add_argument('-v',
                        '--verbose',
                        help="Set verbose option",
                        dest="verbose",
                        required=False,
                        action='store_true')
    parser.add_argument('-d',
                        '--directory',
                        help="Folder with files to upload",
                        dest='input_folder',
                        metavar='STRING',
                        required=False)
    parser.add_argument('-f',
                        '--file',
                        help="File to upload",
                        dest='input_file',
                        metavar='STRING',
                        required=False)
    parser.add_argument('-r',
                        '--remote-folder',
                        help="Remote folder to where upload the file or files",
                        dest='remote_folder',
                        metavar='STRING',
                        required=False)
    parser.add_argument('-b',
                        '--bucket',
                        help="Bucket name",
                        dest='bucket',
                        metavar='STRING',
                        required=True)
    parser.add_argument('-c',
                        '--console-logging',
                        help="Set console logging option",
                        dest="console",
                        required=False,
                        action='store_true')

    return parser


def exit_with_errors(logger, error):  # pragma: no cover
    """ Method to log the last error and exit the application with value 1 """
    logger.error(error)
    sys.exit(1)


def main():  # pragma: no cover
    """ Main method """

    # Get application arguments
    parser = get_arguments()
    args = parser.parse_args()

    # Get verbose argument if passsed
    verbose = True if args.verbose else False

    # Get console argument if passed
    console = True if args.console else False

    # Configure logger
    logger = configure_logger(verbose, console)

    # Input argument is mandatory
    if args.input_folder is None and args.input_file is None:
        parser.print_help()
        exit_with_errors(logger, "At least one argument has to be given!")

    try:
        # Initialize S3Bucket instance
        prg = S3Bucket(name=__application_name__,
                       local_folder=args.input_folder,
                       remote_folder=args.remote_folder,
                       local_file=args.input_file,
                       bucket=args.bucket)
        prg.run()

    # Global catching exceptions because we catch and raise specific exceptions
    # in each class.
    except Exception as error:
        exit_with_errors(logger, error)

    # Exit the application with success
    sys.exit(0)


if __name__ == "__main__":
    main()
