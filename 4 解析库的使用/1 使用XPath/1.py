from lxml import etree

text = ''' <div> 
<Ul> 
<li class="item-O"><a href ="linkl.html"> first item</a><li> 
<li class ="item-1">< a href ="link2.html"> second item</a><li> 
<li class ="item-inactive" >< a href="link3.html"> third item</a></li> 
<li class ="item-1">< a href="link4.html"> fourth item</a><li> 
<li class ＝"item-0"＞＜ a href＝"links.html"＞fifth item</a> 
</ul> 
</div>
'''

html=etree.HTML(text) #调用HTML类初始化,构造了XPath解析对象
result = etree.tostring(html) #输出修正后的html代码，结果是bytes类型
# print(result.decode('utf8'))

#直接读取文本文件进行解析
html2 = etree.parse('./test.html',etree.HTMLParser())
print(etree.tostring(html2).decode('utf8'))


