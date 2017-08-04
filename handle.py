#-*- coding:utf-8 -*- 
# filename: handle.py 

import hashlib 
import web
import generate_token 
import reply
import receive 

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

	def POST(self):
		try:
			print '111111111111111111111111111111111'
			# web.data() 获取实体正文，只能用用POST请求包
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
				
				if recMsg.MsgType == "text":
					content = recMsg.Content
					replyMsg = reply.TextMsg(toUser,fromUser,content)
					# 被动回复消息	
					return replyMsg.send()
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


