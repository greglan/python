# http://docs.python-requests.org/en/master/
import requests
from math import sqrt, floor

IN_URL1 = "https://www.newbiecontest.org/"
OUT_URL = "https://www.newbiecontest.org/"

cookie = {'PHPSESSID': '',
          'SMFCookie89': ''}

r1 = requests.get(IN_URL1, cookies=cookie)
a, b = r1.content.decode('ascii')

r3 = requests.get(OUT_URL+str(y), cookies=cookie)

print(r1.content)

