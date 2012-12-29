#!/usr/bin/python
#
#  Author: Zeng Xi
#  SID:    1010105140
#  Email:  zengxi@cuhk.edu.hk

connected = 0
downloaded_files = ""
total_size = 0

def connect():
	access_key = raw_input('Your access key:').strip()
	secret_key = raw_input('Your secret key:').strip()
	from boto.s3.connection import S3Connection
	global conn 
	conn = S3Connection(access_key, secret_key)
	global connected
	connected = 1

def sync():
	if connected == 0:
		print 'Not connected!\n'
		connect()
	if connected == 1:
		bucket = raw_input('Bucket name:').strip()
		local_path = raw_input('Local directory path:').strip()
		from boto.s3.key import Key
		from hashlib import md5
		b = conn.get_bucket(bucket)
		file_list = b.list()
		for l in file_list:
			try:
				F = open(local_path + l.name,"rb")
			except IOError, e:
				get(bucket, l.name, local_path, l.size)
			else:
				s = md5(F.read()).hexdigest()
				if "\""+str(s)+"\"" == str(l.etag):
					import os
					local_size = os.path.getsize(local_path + l.name)
					if int(local_size) == int(l.size):
						continue
					else:
						get(bucket, l.name, local_path, l.size)
				else:
					get(bucket, l.name, local_path, l.size)
	global downloaded_files
	global total_size
	print "Downloaded files:\n"
	print downloaded_files
	print "Total size:"
	print total_size

def get(bucket, filename, local_path, size):
	global downloaded_files
	global total_size
	downloaded_files += filename + "\n"
	total_size += size
	from boto.s3.key import Key
	b = conn.get_bucket(bucket)
	key = b.lookup(filename)
	key.get_contents_to_filename(local_path + filename)


if __name__ == '__main__':
	sync()
