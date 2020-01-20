import re
import requests
import json
import time

class MAOYAN:

	def __init__(self, url, headers):
		self.url = url
		self.headers = headers

	def get_one_page(self):
		response = requests.get(self.url, headers=self.headers)
		if response.status_code == 200:
			# print(response.text)
			return response.text
		return None

	def parse_one_page(self):
		# p = re.compile('<a href.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?"releasetime">(.*?)</p>$',re.S)
		p = re.compile(
			'<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
		html = self.get_one_page()
		results = p.findall(html)

		for name, actors, time in results:
			yield {
					'name': name,
					'actors': actors.strip()[3:],
					'上映时间': time.strip()[5:]
				 }

	def write_to_file(self,content):
		with open('result.txt','a',encoding='utf8') as f:
			print(json.dumps(content))
			f.write(json.dumps(content,ensure_ascii=False)+'\n')

if __name__ == '__main__':
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) '
		              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
	}
	url = 'http://www.maoyan.com/board/4'

	for i in range(10):
		url2 = url + '?offset=' + str(i * 10)
		mao = MAOYAN(url2, headers)
		# mao.parse_one_page()
		for line in mao.parse_one_page():
			mao.write_to_file(line)
		time.sleep(0.5)