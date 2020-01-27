import requests

r = requests.get('https://www.sex.com/')
print(type(r.status_code), r.status_code)

print(type(r.headers), r.headers)

print('exit') if r.status_code != requests.codes.ok else print('Request Successfully')
