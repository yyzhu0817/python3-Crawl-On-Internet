from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener
from urllib.error import URLError

username = 'admin'
passward = 'yyzhu727'
url = 'http://192.168.0.1'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,passward)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
	result = opener.open(url)
	html = result.read().decode('utf8')
	print(html)
except URLError as e:
	print(e.reason)