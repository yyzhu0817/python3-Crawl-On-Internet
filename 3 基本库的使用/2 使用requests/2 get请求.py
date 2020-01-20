import requests

data = {
	'name':'tt',
	'age':12
}
r = requests.get('http://httpbin.org/get',params=data)
print(r.text)

print('-'*20)

print(r.json())