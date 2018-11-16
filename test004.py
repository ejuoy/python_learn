#!/usr/bin/env python
#-*- coding:utf8-*-

'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
import time
print(time.asctime(time.localtime()),"test004")
year=int(input("please input year\n"))
mouth=int(input("please input mouth\n"))
day=int(input("please input day\n"))

print("%d-%d-%d"%(year,mouth,day))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

sum = 0
if((year%400)==0 or (year%4==0 and year%100!=0)):
	if(mouth>2):
		sum +=1

sum+=( months[mouth] + day)
print("sum = %d" %sum) 

'''
元组 和 列表
'''

