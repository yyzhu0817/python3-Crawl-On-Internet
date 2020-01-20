import re

content = '12lgklgj123bkljb5k3k2b12b31k'
content = re.sub('\d+',' ',content)
print(content)