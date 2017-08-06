#-*- coding:utf-8 -*-
# filename: reply.py
import time

class Msg(object):
	def __init_(self):
		pass
	def send(self):
		return "success"
	
class TextMsg(Msg):
	def __init__(self,toUserName,fromUserName,content):
		self.__dict = dict() 
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time()) 
		self.__dict['Content'] = content

	def send(self):
		XmlForm = """
		<xml>
			<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
			<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
			<CreateTime><![CDATA[{CreateTime}]]></CreateTime>
			<MsgType><![CDATA[text]]></MsgType>
			<Content><![CDATA[{Content}]]></Content>
		</xml>
		"""
		print XmlForm.format(**self.__dict)
		return XmlForm.format(**self.__dict)

class ImageMsg(Msg):
	def __init__(self,toUserName,fromUserName,mediaId):
		print "@@@@@@@@@11111111111"
		self.__dict = dict()
		self.__dict['ToUserName'] = toUserName
		self.__dict['FromUserName'] = fromUserName
		self.__dict['CreateTime'] = int(time.time())
		self.__dict['MediaId'] = mediaId
		print "@@@@@@222222222222222"

	def send(self):
		XmlForm = """
		<xml>
			<ToUserName><![CDATA[{ToUserName}]]></ToUserName>
			<FromUserName><![CDATA[{FromUserName}]]></FromUserName>
			<CreateTime><![CDATA[{CreateTime}]]></CreateTime>
			<MsgType><![CDATA[image]]></MsgType>
			<Image>
				<MediaId><![CDATA[{MediaId}]]></MediaId>
			</Image>
		</xml>
		"""

		return XmlForm.format(**self.__dict)


