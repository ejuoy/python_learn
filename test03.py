#!/usr/bin/env python
#-*- coding:utf8 -*-

import time
print(time.asctime(time.localtime()),'test03')

def fun1(str):
	print(str)
	pass
fun1('hello,fun')

def fun2(a,b):
	a += 1;
	b -= 1;
	print('fun',a,b)

a = 3
b = 4
fun2(a,b)
print(a,b)

c = [1,2,3,4]
d = 'youjie'

def fun3(c,d):
	c[0] = 10
	d = d * 4
	print("fun",c,d)
fun3(c,d)
print(c,d)



