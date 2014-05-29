#!/usr/bin/env python
#-*- coding:utf-8-*-
import socket
import thread
import time,os,shutil,platform,datetime,sys,string
import urllib2
import re


#读取文件
myfile = open("aa.txt")
file_object = open('bb.txt', 'w')
for line in myfile.readlines():
	response = urllib2.urlopen(line[0:-1])
	headers = response.info()
	data = response.read()
	pattern = re.compile(r"[\s\S]*FileUtils\.share_uk=\"(\d+)\";FileUtils\.share_id=\"(\d+)\";[\s\S]*")
	match = pattern.match(data)
	result = 'http://pan.baidu.com/share/link?'
	if match:
	    # 使用Match获得分组信息
	    result += 'shareid=' + match.group(2)
	    result += '&uk=' + match.group(1)
	print result 

	file_object.writelines(result + '\r\n')

myfile.close()
file_object.close()


 

  
