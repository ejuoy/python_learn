#!/usr/bin/usr python
#-*- coding:utf8 -*-


import logging 
import os
  
# 创建一个logger 
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG) 
  
# 创建一个handler，用于写入日志文件 
fh = logging.FileHandler('fork.log') 
fh.setLevel(logging.DEBUG) 
  
# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG) 
  
# 定义handler的输出格式 
formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
  
# 给logger添加handler 
logger.addHandler(fh) 
logger.addHandler(ch) 

logger.info("fork test %d"%os.getpid())

pid = os.fork()
if(pid == 0):
	logger.info("child process %d"%os.getpid())
else:
	logger.info("create child %d"%os.getpid())







