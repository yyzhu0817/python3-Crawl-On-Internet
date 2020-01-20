import re
import requests

headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)

titles = re.findall(pattern,r.text)
# print(r.text)
print(titles)