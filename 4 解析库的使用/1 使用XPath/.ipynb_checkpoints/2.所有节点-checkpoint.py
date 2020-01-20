from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')
print(result)

result2 = html.xpath('//li')
print(result2)
print(result2[0])