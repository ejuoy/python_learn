#!/user/bin/env python
import time ,threading
import logging 
  
# 创建一个logger 
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG) 
  
# 创建一个handler，用于写入日志文件 
fh = logging.FileHandler('test.log') 
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
  

def fun_1():
	logger.info("fun %s"%threading.current_thread().name)
	for i in range(1,10):
		time.sleep(1)
		logger.info(" test %d"%i)
# 记录一条日志 
logger.info('pthread ') 
t = threading.Thread(target=fun_1,name='test_fun')
t.start()
t.join()
logger.info('pthread end')
