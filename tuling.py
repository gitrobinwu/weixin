#-*- coding:utf-8 -*- 
# tuling.py 

import urllib,urllib2 
import json 

def reply_text(msg):
	if type(msg) == type(""):
		info = msg 
	else:
		info = msg.encode('utf-8')

	api_url = "http://www.tuling123.com/openapi/api"
	api_key = "bccfa0160f6d4d16af03aa5bf372a12e"
	
	data = {
		"key": api_key,
		"info": info,
		"userid": "120317"
	}
	data = urllib.urlencode(data)

	try:	
		request = urllib2.Request(api_url,data)
		response = urllib2.urlopen(request)
		result = response.read()
		result = json.loads(result)
		return  result['text']

	except urllib2.URLError,e:
		if hasattr(e,"reason"):
			print "We failed to reach a seaver."
			print "Reason:",e.reason 
		elif hasattr(e,'code'):
			print "The server count/'t fulfill the request."
		else:
			pass 


if __name__ == "__main__":
	import sys
	#print type(sys.argv[1])
	print reply_text("%s" % sys.argv[1])



