import requests

r = requests.get('https://www.github.com/favicon.ico')
# print(r.text) 转化为字符串类型，会出现乱码
print(r.content)  # 转化为字节类型

with open('favicon.ico', 'wb') as f:
    f.write(r.content)
