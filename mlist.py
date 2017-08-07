#-*- coding:utf-8 -*- 
import os
import re
def music_list():
	url = 'http://wuyongwei.applinzi.com/'
	music_link = [url+x for x in os.listdir('./static/')]	
	music_name = [re.sub("\.mp3","",x) for x in os.listdir('./static')]
	return [[x,y,"我爱范晶"] for x in music_link for y in music_name]

if __name__ == "__main__":
	for x in music_list():
		print x[0],x[1],x[2]



