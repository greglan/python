# http://docs.python-requests.org/en/master/
import requests
from math import sqrt, floor

IN_URL1 = "http://challenge01.root-me.org/programmation/ch1/"
OUT_URL = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="

cookie = {'PHPSESSID': '',
          'SMFCookie89': ''}

r1 = requests.get(IN_URL1, cookies=cookie)
challenge = r1.content.decode('ascii')

a = 0
b = 0
u_0 = 34
n = 4000

y = u_0 + n/2 * (2*a + b*(n-1))

r3 = requests.get(OUT_URL+str(y), cookies=cookie)

print(r1.content)

