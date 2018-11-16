#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义
'''

import time
print(time.asctime(time.localtime()),'test006')

def Fibonacci(pos):
	a,b = 0,1
	while pos>0:
		pos -= 1
		a,b = b , a+b
		print(a,b)
	return a
Fibonacci(10)

'''
赋值运算,先计算 =  左边
a,b = b,a+b
b = 1,a+b = 1
a = 1, b = 1
'''

a=[1,2,3]
b=a[:]		# 列表复制
print(b)


