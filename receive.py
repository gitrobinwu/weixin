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
		print "6666666666666666666666"
	elif msg_type == 'image':
		return ImageMsg(xmlData)

class Msg(object):
	def __init__(self,xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xml.Data.find('MsgId').text 

class TextMsg(Msg):
	def __init__(self,xmlData):
		print "888888888888888888888"
		super(TextMsg,self).__init__(xmlData)
		self.Content = xmlData.find('Content').text.encode('utf-8')

class ImageMsg(Msg):
	def __init__(self,xmlData):
		super(ImageMsg,self).__init__(xmlData)
		self.Content = xmlData.find('Content').text.encode('utf-8')



