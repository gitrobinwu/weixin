#-*- coding:utf-8 -*- 
# filename: handle.py 
import os 
import json 
import hashlib 
import web
import generate_token 
import reply
import receive 

class Handle(object):
	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.templates_root)

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

	def send_text(touser,fromuser,content):
		replyMsg = reply.TextMsg(tousr,fromuser,content)
		return replyMsg

	def POST(self):
		try:
			webData = web.data()
			print 'Handle Post webdata is ',webData # 后台打印日志
			# 解析xml 
			print "satrt ----- parse_xml --------"
			recMsg = receive.parse_xml(webData)
			print "7777777777777777777777777"
			print "-"*80
			print recMsg,recMsg.MsgType
			print "-"*80

			# 文本消息
			if isinstance(recMsg, receive.Msg):
				print '22222222222222222222222222222222222'
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
			
				if recMsg.MsgType == "event":
					if recMsg.Event == "subscribe":
						content = u"欢迎关注本微信"
						return self.send_text(toUser,fromUser,content)
		
					if recMsg.Event == "unsubscribe":
						content = u"欢迎您再来"
						return self.send_text(toUser,fromUser,content)

				if recMsg.MsgType == "text":
					print "3333333333333333333333333333"
					# 文本消息处理
					content = recMsg.Content
					if content.find("help") != -1:
						print "4444444444444444444444"
						content = u'''1.输入中文或者英文返回对应的英中翻译\n2.输入 book 要查询的书名 返回豆瓣图书中结果\n3.输入cls清除查询记录\n4.输入m随机来首音乐听，建议在wifi下听\n5.输入python 进入python常用模块用法查询（未完成）'''
						return self.send_text(toUser,fromUser.content)	
					print "55555555555555555555555555555555555"
					return self.send_text(toUser,fromUser.content)
							
				elif recMsg.MsgType == "image":
					print "AAAAAAAAAAAAAAAAAAAAAAA"
					MediaId = recMsg.MediaId
					print MediaId
					replyMsg = reply.ImageMsg(toUser,fromUser,MediaId)
					print "BBBBBBBBBBBBBBBBBBBBB"
					replyMsg = replyMsg.send()
					print replyMsg
					return replyMsg
				else:
					return reply.Msg().send()

			else:
				print u"暂不处理"
				return reply.Msg().send() 
		except Exception,Argment:
			return Argment


			
			
if __name__ == '__main__':
	print generate_token.hash


