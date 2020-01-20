from urllib import request,error
try:
	response = request.urlopen('http://zhuyangyang.xyz/index.htm')
	print(response.read().decode('utf8'))
except error.HTTPError as e:
	print(e.reason,e.code,e.headers)
except error.URLError as e:
	print(e.reason)
