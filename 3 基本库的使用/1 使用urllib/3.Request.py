import urllib.request as req
import urllib.parse as parse

url = 'http://httpbin.org/post'
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
	'Host':'httpbin.org'
}
data = bytes(parse.urlencode({'name':'ABC'}),encoding='utf8')
request = req.Request(url=url,headers=headers,data=data,method='POST')
response = req.urlopen(request)
print(response.read().decode('utf8'))