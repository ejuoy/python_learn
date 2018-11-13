#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
	有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
import time
i=0
print(time.asctime(time.localtime()),"test001")
for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			if(a!=b and b!=c and a!=c):
					print("%d\t%d\t%d"%(a,b,c))
					i += 1
print("test 001 over count %d"%i)


'''
		if(a!=b&&b!=c&&a!=c):
		python中取消了&& 与 或  去而代替的  and or
	
		i++ ++i python中无 写法
		i = 2
		++ i
		+(+)i
		-(-)i
		++ -- 写在前面实现符号运算操作
'''

'''
for 循环 
 	range 函数的使用
'''

