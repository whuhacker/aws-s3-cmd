aws-s3-cmd
==========

Amazon S3 Command Line Interface

Introduction
------------

This tool provides a command line interface to AWS S3 service.

Supported commands:
* `connect`         Get user credential and connect to Amazon S3
* `creat`           Creat bucket
* `put`             Upload file to S3
* `ls`              List buckets
* `lsfile`          List files in a bucket
* `info`            Display information of a file
* `permission`      Set bucket permissions
* `get`             Download file from S3
* `delete`          Delete bucket
* `delfile`         Delete file
* `quit`            Quit
 
You can also synchronize files between your local machine and the Amazon S3 storage. Just like what Dropbox does. It will check the file name, size, and MD5 when you run this script. If there is any difference between S3 bucket and local directory, it will download the additional files in S3 to your disk.

More details: [Amazon S3 云存储服务 Cloud Storage (in Chinese)](http://www.lovelucy.info/amazon-s3-interface.html)

System Requirement
------------------

Python >= 2.7.1

boto >= 2.0

```bash
# Install boto via pip:
$ pip install boto

# Install boto from source:
$ git clone git://github.com/boto/boto.git
$ cd boto
$ python setup.py install
```

Usage
-----

S3 cmd:
```bash
$ python s3.py
```

S3 sync:
```bash
$ python sync.py
```
