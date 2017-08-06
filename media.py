#-*- coding:utf-8 -*- 
# filename: media.py
from basic import Basic 
import os 
import json 

filePath = "/home/robin/weixin/test/images/0.jpg" 
accessToken = Basic().get_access_token()
mediaType = "image"

cmd = "curl -F media=@%s 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s'" % (filePath,accessToken,mediaType)

rst = os.popen(cmd).read()
rst = json.loads(rst)
print rst['type'],rst['media_id'],rst['created_at']

print '-'*60 
cmd1 = "curl 'https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s'" % (accessToken,rst['media_id'])

rst1 = os.popen(cmd).read()
print rst1 
