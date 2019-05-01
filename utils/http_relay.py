# http://docs.python-requests.org/en/master/
import requests
from math import sqrt, floor

IN_URL1 = "http://challenge01.root-me.org/programmation/ch1/"
OUT_URL = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="

cookie = {'PHPSESSID': '',
          'SMFCookie89': ''}

r1 = requests.get(IN_URL1, cookies=cookie)
challenge = r1.content.decode('ascii')

y = 0

r3 = requests.get(OUT_URL+str(y), cookies=cookie)

print(r1.content)

