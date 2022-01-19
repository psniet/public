import time
import os

for n in range(1,50001):
	if n%10==0:
		print("started sync")
		time.sleep(600)
		print("sync finished")
	e = os.system('echo "this is test {}" > file{}.txt'.format(n,n))
	os.system('cnvrg data put ds2 .')
	print("file generated {}".format(n))
