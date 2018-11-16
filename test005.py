#!/usr/bin/env python
#-*- coding:utf8-*-

'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''

L=[]
for i in range(3):
	num=int(input("please input num\n"))
	L.append(num)
L.sort()
print(L)

