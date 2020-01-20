def square(): #生成器函数被调用后，函数体内的代码不会立即执行，而是返回一个生成器
	for i in range(4):
		yield i**2

for j in square():#当返回的生成器调用成员方法时，相应的生成器函数中代码才会执行
	print(j)