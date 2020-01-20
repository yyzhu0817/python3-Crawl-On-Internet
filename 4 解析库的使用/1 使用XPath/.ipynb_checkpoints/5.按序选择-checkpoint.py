from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[1]/a/text()')
print(result)

result = html.xpath('//li[last()]/a/text()')
print(result)

result2 = html.xpath('//li[position()<3]/a/text()')
print('position()<3的节点',result2)
