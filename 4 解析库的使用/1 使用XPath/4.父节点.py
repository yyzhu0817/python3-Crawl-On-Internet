from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

#属性匹配
result2 = html.xpath('//li[@class="item-0"]')
print('result2=',result2)

#文本获取
result3 = html.xpath('//li[@class="item-0"]//text()')
print(result3)

#属性获取
result4 = html.xpath('//li/a/@href')
print(result4)

#属性多值匹配
text2 = '''
	<li class="li li-first"><a href="link.html">first item</a> </li>
'''
html2 = etree.HTML(text2)
result5 = html2.xpath('//li[contains(@class,li)]//text()')
print('result5=',result5)