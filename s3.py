#!/usr/bin/python
#
#  Amazon S3 Interface
#  Author: Zeng Xi
#  SID:    1010105140
#  Email:  zengxi@cuhk.edu.hk
connected = 0

def connect():
	access_key = raw_input('Your access key:').strip()
	secret_key = raw_input('Your secret key:').strip()
	from boto.s3.connection import S3Connection
	global conn 
	conn = S3Connection(access_key, secret_key)
	global connected
	connected = 1

def creat():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		bucket_name = raw_input('Bucket name:').strip()
		bucket = conn.create_bucket(bucket_name)

def put():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		local_file = raw_input('Local filename:').strip()
		bucket = raw_input('Target bucket name:').strip()
		from boto.s3.key import Key
		b = conn.get_bucket(bucket)
		k = Key(b)
		k.key = local_file
		k.set_contents_from_filename(local_file)

def ls():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		rs = conn.get_all_buckets()
		for b in rs:
			print b.name

def lsfile():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		bucket = raw_input('Bucket name:').strip()
		from boto.s3.key import Key
		b = conn.get_bucket(bucket)
		file_list = b.list()
		for l in file_list:
			print l.name

def info():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		bucket = raw_input('Bucket name:').strip()
		filename = raw_input('Filename:').strip()
		from boto.s3.bucketlistresultset import BucketListResultSet
		b = conn.get_bucket(bucket)
		brs = BucketListResultSet(bucket=b)
		for f in brs:
			key = b.lookup(f.name)
			print 'File: ' + f.name
			print 'size: ' + str(key.size)
			print 'last modified: ' + str(key.last_modified)
			print 'etag (md5): ' + str(key.etag)

def permission():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		while True:
			bucket = raw_input('Bucket name:').strip()
			permission = raw_input('Permission (private or public-read):').strip()
			if permission not in ['private', 'public-read']:
				print 'Input error!'
			elif permission in ['private', 'public-read']:
				break
		b = conn.get_bucket(bucket)
		b.set_acl(permission)

def get():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		bucket = raw_input('Source bucket name:').strip()
		s_file = raw_input('Source filename:').strip()
		d_file = raw_input('Local directory path and filename:').strip()
		from boto.s3.key import Key
		b = conn.get_bucket(bucket)
		key = b.lookup(s_file)
		key.get_contents_to_filename(d_file)

def delete():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		bucket = raw_input('Bucket name:').strip()
		conn.delete_bucket(bucket)

def delfile():
	if connected == 0:
		print 'Not connected!'
	elif connected == 1:
		bucket = raw_input('Bucket name:').strip()
		filename = raw_input('Filename:').strip()
		b = conn.get_bucket(bucket)
		b.delete_key(filename)

def showMenu():
	title = '''
		Amazon S3 Service

	connect		Get user credential and connect to Amazon S3
	creat		Creat bucket
	put		Upload file to S3
	ls		List buckets
	lsfile		List files in a bucket
	info		Display information of a file
	permission	Set bucket permissions
	get		Download file from S3
	delete		Delete bucket
	delfile		Delete file
	quit		Quit

Enter choice:'''
	while True:
		choice = raw_input(title).strip().lower()
		choices =  ['connect','creat','put','ls','lsfile','info','permission','get','delete','delfile','quit']
		if choice not in choices:
			print('Input Error!')
		else:
			if choice == 'quit':
				break
			elif choice == 'connect':
				connect()
			elif choice == 'creat':
				creat()
			elif choice == 'put':
				put()
			elif choice == 'ls':
				ls()
			elif choice == 'lsfile':
				lsfile()
			elif choice == 'info':
				info()
			elif choice == 'permission':
				permission()
			elif choice == 'get':
				get()
			elif choice == 'delete':
				delete()
			elif choice == 'delfile':
				delfile()
if __name__ == '__main__':
	showMenu()

