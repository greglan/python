#!/usr/bin/env python
import httplib,urllib;
import time;

n = 2;
i = 0;
conn = httplib.HTTPConnection('hd1.freebox.fr');
params = urllib.urlencode({
   "app_id": "fr.freebox.testapp",
   "app_name": "Test App",
   "app_version": "0.0.7",
   "device_name": "Pc de Xavier"
})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

while (i <= n):
	conn.request('POST', '/api/v3/login/authorize/',params, headers);
	res = conn.getresponse();
	print(i, res.status, res.reason);
	time.sleep(1);
	i+=1;

conn.close();



