import urllib.request as req

response = req.urlopen('https://www.baidu.com',)
# print(type(response))
# print(response.read().decode('utf-8'))
print(response.status)
print(response.getheader('server'))
