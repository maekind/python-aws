<!-- Shields -->
[![licence](https://img.shields.io/badge/License-MIT-orange.svg)](https://github.com/maekind/python-aws/blob/main/LICENSE)
[![python_version](https://img.shields.io/badge/python%20version-%3E3.10-blue)](https://www.python.org/downloads/release/python-3110/)
[![size](https://img.shields.io/github/repo-size/maekind/python-aws)](https://github.com/maekind/python-aws)
[![last_commit](https://img.shields.io/github/last-commit/maekind/python-aws?color=violet)](https://github.com/maekind/python-aws)
[![language](https://img.shields.io/github/languages/top/maekind/python-aws?color=yellowgreen)](https://github.com/maekind/python-aws)

# Python AWS 🐍

## Description

This project means to be an AWS library, providing access to several AWS objects.
For now, only the upload function is provided.

## Environment configuration

In order to setup the virtual environment, we can follow the next statements.

For pipenv installation: 

`$> pip install --upgrade pip && pip install pipenv`

Then, you have to install the required packages.

`$> pipenv install`

To activate the virtual environment, exceute the following command:

`$> pipenv shell`

## Default application arguments

### Uploading files

A main.py file is provided in the root folder.
The main program defines the following parameters by default:
- -v / --verbose [optional]: flag to let know the application to show debug messages. By default, logging is configured in the INFO level. So, debug messages won't be shown.
- -c / --console-logging [optional]: flag to let know the application to show logging messages in to the standard output. By default, logging is performed to a log file.
- -d / --directory [optional]: Folder with files to upload.
- -f / --file [optional]: File to upload.
- -r / --remote [optional]: Remote folder to where upload the file or files.
- -b / --bucket: The S3 bucket name.  

NOTA: At least a directory or a file has to be provided.

## AWS credentials

AWS id and secret token pair values are stored in your local machine. 
Follow this link for more information on [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Examples

### Upload a file to a bucket

`$> python3 main -b my-bucket -f my-file.txt`

### Upload a complete folder and subdolfers to a bucket

`$> python3 main -b my-bucket -d my-folder`

### Upload a file to specific folder in to a bucket

`$> python3 main -b my-bucket -f my-file.txt -r folder1/subfolder3`



<!-- ## Contributors

<a href="https://github.com/maekind/python-aws/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=maekind/python-aws" />
</a>

<a href="mailto:marco@marcoespinosa.es">Say hello!</a> -->
