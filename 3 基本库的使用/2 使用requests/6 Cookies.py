import requests

headers = {
	'cookie':'_xsrf=73ca499f-70d8-41c7-ad15-b3dae5d22c15; _zap=387748a9-f5f7-49c7-8137-35cabc924371; d_c0="AKDhg_Jxyg-PTqEClkB-CWE4KBypjC4UPJU=|1564063898"; ISSW=1; capsion_ticket="2|1:0|10:1577120053|14:capsion_ticket|44:ZmI2NmQ1MDYyNzQwNGNhMjllMjBlNjhlMWFhYTJjMDc=|8c53cb10cd3b0ccd7fd59bba4dd8024bf2ebe85c7cddeffd1e825ef67f2bb012"; z_c0="2|1:0|10:1577120058|4:z_c0|92:Mi4xekt3VUFBQUFBQUFBb09HRDhuSEtEeVlBQUFCZ0FsVk5Pal91WGdBdHZGTm5uWjFhTE0zR0RxeVJfUWl1WC1Gc3ZR|cf90c5db6fc1c35628acbc398d2718b5e8357ce4f9546132c3b5a61a24afb129"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1577058241,1577064227,1577065260,1577136355; q_c1=c17ca7ef6bff444ebefc2dd769bcf56a|1577136355000|1577136355000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1577198680',
	'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

r = requests.get('https://www.zhihu.com',headers=headers)
# print(r.cookies)
# print(r.cookies.items())
# for key,value in r.cookies.items():
# 	print(key + '=' + value,sep='\n')

print(r.text)