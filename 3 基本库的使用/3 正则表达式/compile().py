import re

content1 = '2006-12-15 12:00'
content2 = '2005-12-52 13:12'
content3 = '2013-02-12 14:23'

pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub('\d{2}:\d{2}','',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)

print(result1,result2,result3)
