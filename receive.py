#-*- coding:utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

# 解析XML数据文档
def parse_xml(web_data):
	#  异常判断
	if len(web_data) == 0:
		return None 
	
	# 加载XML文件 
	xmlData = ET.fromstring(web_data)
	msg_type = xmlData.find('MsgType').text

	# 处理不同类型的消息事件 
	if msg_type == "event":
		return EventMsg(xmlData)
	if msg_type == 'text':
		return TextMsg(xmlData)
	elif msg_type == 'image':
		return ImageMsg(xmlData)

class Msg(object):
	def __init__(self,xmlData):
		print "************************"
		self.ToUserName = xmlData.find('ToUserName').text
		print "***111111111"
		self.FromUserName = xmlData.find('FromUserName').text
		print "****2222222"
		self.CreateTime = xmlData.find('CreateTime').text
		print "****33333333"
		self.MsgType = xmlData.find('MsgType').text
		print "*****444444"
		print "9999999999999999999999999999"

class TextMsg(Msg):
	def __init__(self,xmlData):
		print "888888888888888888888"
		super(TextMsg,self).__init__(xmlData)
		print "&&&&&&&&&&&&&&&&&&&&"
		self.Content = xmlData.find('Content').text.encode('utf-8')
		self.MsgId = xmlData.find('MsgId').text 

class ImageMsg(Msg):
	def __init__(self,xmlData):
		print "$$$$$$$$$$$22222222222"
		Msg.__init__(self, xmlData)
		self.PicUrl = xmlData.find('PicUrl').text
		self.MediaId = xmlData.find('MediaId').text
		self.MsgId = xmlData.find('MsgId').text 
		print "$$$$$$$$$$$$$3333333333"


class EventMsg(Msg):
	def __init__(self,xmlData):
		super(EventMsg,self).__init__(xmlData)
		self.Event = xmlData.find('Event').text


