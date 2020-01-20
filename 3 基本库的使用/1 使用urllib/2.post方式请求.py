import urllib.request as request
import urllib.parse as parse
import socket
import urllib.error

try:
	data = bytes(parse.urlencode({'world':'hello'}),encoding='utf8')
	response = request.urlopen('http://httpbin.org/post',data=data,timeout=0.1,)
	print(response.read().decode('utf8'))
except urllib.error.URLError as e:
	if isinstance(e.reason,socket.timeout):
		print('TIME OUT')
