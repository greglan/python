#!/usr/bin/env python
import httplib;
import time;

n = 10**5
i = 0
conn = httplib.HTTPConnection('hd1.freebox.fr')

while (i <= n):
	conn.request('GET', '/pub/remote_control?code=27266552&key=power')
	res = conn.getresponse()
	print(i, res.status, res.reason);
	time.sleep(1)
	i+=1

conn.close()



