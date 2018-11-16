#!/usr/bin/env python
#-*-coding:utf8 -*-


```

日志库的使用
和简单的配置

```
import time
import logging
print("test_log\t",end='')
print('hello')

print(time.asctime(time.localtime()))

LOG_FORMAT="%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT="%m/%d/%Y %H:%M:%S %p"

#logging.basicConfig(filename='my.log',level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT)
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT)

logging.debug("first usring logging")
logging.info("info usring logging")
logging.error("error usring logging")
logging.warning("error usring logging")
logging.critical("critical using logging")

