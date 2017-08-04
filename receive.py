#-*- coding:utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET

def parse_xml(web_data):
	if len(web_data) == 0:
		return None 
	
	print "33333333333333333333333"
	# 加载XML文件 
	xmlData = ET.fromstring(web_data)
	msg_type = xmlData.find('MsgType').text
	print "444444444444444444444"
	if msg_type == 'text':
		print "555555555555555555555"
		textobj =  TextMsg(xmlData)
		print textobj.Content,textobj.MsgType
		print "6666666666666666666666"
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
		self.MsgId = xml.Data.find('MsgId').text 
		print "9999999999999999999999999999"

class TextMsg(Msg):
	def __init__(self,xmlData):
		print "888888888888888888888"
		Msg.__init__(self, xmlData)
		print "&&&&&&&&&&&&&&&&&&&&"
		self.Content = xmlData.find('Content').text.encode('utf-8')

class ImageMsg(Msg):
	def __init__(self,xmlData):
		Msg.__init__(self, xmlData)
		self.Content = xmlData.find('Content').text.encode('utf-8')



