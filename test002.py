#!/usr/bin/env python
#-*- coding:utf8-*-

'''
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
import time

flag = 0
num = 0
print(time.asctime(time.localtime()),"test 002")
for i in range(1,10000):
	flag = 0
	num = 0
	for j in range(1,100):
		if(flag==0):
			if(j*j==i+100):
				num = i
				#print("%d*%d=%d i = %d + 100" %(j,j,i+100,i))
				flag=1
				#continue
		else:
			if(j*j==i+168):
				print("%d*%d=%d i = %d + 168" %(j,j,i+168,i))
				print("%d*%d=%d i = %d + 100" %(num,num,i+100,i))
				break
			else:
				pass




