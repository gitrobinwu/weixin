#-*- coding:utf-8 -*- 
# filename: basic.py 

import urllib
import time 
import json

class Basic:
	def __init__(self):
		self.__accessToken = ""
		self.__leftTime = 0
	
	def __real_get_access_token(self):
		appId = "wxac227566880e5062"
		appSecret = "9330ff952a586cae7596a5401fc80488"

		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
		urlResp = urllib.urlopen(postUrl)
		# 将json字符串转换成python 字典对象	
		urlResp = json.loads(urlResp.read())
		
		self.__accessToken = urlResp['access_token']
		self.__leftTime = urlResp['expires_in']

	def real_get(self):
		self.__real_get_access_token() 

	def get_access(self):
		return self.__accessToken
	def get_left(self):
		return self.__leftTime

	def get_access_token(self):
		print "beforet "
		print 'self.__leftTime:',self.__leftTime
		print 'self.__accessToken:',self.__accessToken
		print "-"*60 

		if self.__leftTime < 10:
			self.__real_get_access_token()

		print 'self.__leftTime:',self.__leftTime 
		return self.__accessToken

	def run(self):
		while(True):
			if self.__leftTime > 10:
				time.sleep(2)
				self.__leftTime -= 2
			else:
				self.__real_get_access_token() 


if __name__ == '__main__':
	b = Basic()
	a = b.get_access_token()
	print '__accessToken:',a 
	#print b.get_left()
	#print b.get_access() 


