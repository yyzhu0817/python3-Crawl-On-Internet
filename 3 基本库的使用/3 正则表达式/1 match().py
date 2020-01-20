import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())

print('############################################################################')
content = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\sWorld',content)
print(result2)
print(result2.group())
print(result2.group(1))

print('############################################################################')

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())

print('############################################################################')

content = '''abcHello 1234567 World_This
            is a Regex Demo'''
result = re.search('He.*?(\d+).*Demo',content,re.S)
print(result)
print(result.group(1))

