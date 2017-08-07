#-*- coding:utf-8 -*- 
# filename: handle.py 
import os 
import time 
import json 
import hashlib 
import web
import generate_token 
import reply
import receive 
import tuling 
import musiclist 
import random 

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

	def send_text(self,touser,fromuser,content):
		print "6666666666666666666666666"
		print touser,fromuser,content 
		replyMsg = reply.TextMsg(touser,fromuser,content).send() 
		print "7777777777777777777777777777"
		print replyMsg
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
						response = "this is a test"*10 
						return self.send_text(toUser,fromUser,response)	
					if content.lower() == "m":
						print "mmmm 1111111111111111"
						musicList = musiclist.get_musiclist()
						print "mmmmm 33333333333333"
						music = random.choice(musicList)
						print "mmmmmm 444444444444"
						print music
						music_url = music[0]
						music_title = music[1]
						music_des = music[2]
						print "mmmmmmm 2222222222222"
						#$def with(toUser,fromUser,createTime,musicTitle,musicDes,musicURL)
						music_xml = self.render.reply_music(toUser,fromUser,int(time.time()),music_title,music_des,music_url)
						print music_xml
						return music_xml

					if content.find("爱你") != -1:
						response = u"我爱范晶"
						return self.send_text(toUser,fromUser,response)	
					response= tuling.reply_text(content) 	
					print "55555555555555555555555555555555555"
					return self.send_text(toUser,fromUser,response)	
							
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

	def test(self):
		print self.render.reply_text("fromUser","toUser",int(time.time()),"this is a test")
		print self.render.reply_music("fromUser","toUser",int(time.time()),"title","des","musicull")
			
			
if __name__ == '__main__':
	#print generate_token.hash
	#Handle().test() 	
	print musiclist.get_musiclist()


