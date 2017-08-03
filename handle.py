#-*- coding:utf-8 -*- 
# filename: handle.py 

import hashlib 
import web
import generate_token 

class Handle(object):
	def GET(self):
		try:
			# 接收数据[不确定是谁发过来的]
			# 尝试提取出signature,timestamp,nonce,echostr字段
			# 提取不成功不处理
			data = web.input()
			if len(data) == 0:
				return "hello,this is handle view"
			signature = data.signature 
			timestamp = data.timestamp
			nonce = data.nonce 
			echostr = data.echostr
			# 验证开发服务器
			token = generate_token.hash 

			# token,timestamp,nonce字典排序得到字符串list
			list = [token,timestamp,nonce]
			list.sort()
			# 哈希算法加密list得到hashcode 
			sha1 = hashlib.sha1()
			map(sha1.update,list)
			hashcode = sha1.hexdigest()
			
			print "handle/GET func: hashcode,signature: ",hashcode,signature
			# 判断hashcode == signature 服务器确定数据源是否是微信后台
			# no 不处理
			# yes -->把echostr返回给微信后台，供微信后台认证token (开发服务器) 
			if hashcode == signature:
				return echostr
			else:
				return ""
		except Exception,Argument:
			return Argument


