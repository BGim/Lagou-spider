#-*-coding:utf-8-*-
import os
import sys
import signal
import logging
import win32api

logging.basicConfig(filename = 'log/shutdown.log', format = '%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO)

logging.info("info")
logging.warn("Loging Start!")

def handler(signum,frame):
	logging.error("Force exit on %s"%(signum))
	sys.exit(1)
'''while True:
	signal.signal(signal.SIGINT,handler)
	signal.signal(signal.SIGBREAK,handler)
	signal.signal(signal.SIGTERM,handler)
	signal.signal(signal.SIGABRT,handler)
	signal.signal(signal.SIGFPE,handler)
	signal.signal(signal.SIGSEGV,handler)'''
'''with open('recode/data.txt','r') as f:
    	data=f.readlines()
	print(data[0].strip())'''

print('\n\n\n%s\t%5s\t'%('\t'*2,'爬虫程序正在运行！'))

print('\n\n\t%s'%('*'*57))
print('\t*\t%5s\t%s*'%('请不要关闭当前对话，如需关闭。','\t'*2))
print('\t*\t%5s\t*'%('请用Ctrl+C使数据完整保存后，再关闭对话框。'))
print('\t*\t%5s\t*'%('请用Ctrl+C使数据完整保存后，再关闭对话框。'))
print('\t*\t%5s\t%s*'%('请不要关闭当前对话，如需关闭。','\t'*2))
print('\t%s'%('*'*57))

