from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class ="title" name="dromouse"><b>The Dormouse's story</b> </p>
<p class ="story"> Once upon a time there were three little sisters; and their names were
<a href ="http://example.com/elsie" class= "sister" id ="link1"><!-- Elsie --></a>,
<a href ="http://example.com/lacie" class ="sister" id ="link2"> Lacie</a> and
<a href="http://example.com/tillie" class ="sister" id ="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class ="story"> ... </p>
'''

soup2 = BeautifulSoup(html,'lxml') #使用lxml解析器类型进行解析
print(soup2.prettify())
print(soup2.title.string)

print('---'*30)

print(soup2.title)
print(type(soup2.title))
print(soup2.head)
print('soup2.p is ','\n',soup2.p)

print('---'*30)

print(soup2.title.name) #获取节点名称
print(soup2.p.attrs)
print(soup2.p['name'])
print(soup2.p['class'])

