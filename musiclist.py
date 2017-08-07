#-*- coding: utf-8 -*-
import urllib2
import re
import urllib
from json import *

category = '经典老歌'
url = 'http://music.baidu.com/tag/' + category
url_songs = 'http://play.baidu.com/data/music/songlink'

def get_musiclist():
	try:
		request = urllib2.Request(url)
		response =urllib2.urlopen(request)
		content = response.read() 
		# &quot; == " 获取songIds 
		patt_str = '<li data-songitem = \'{&quot;songItem&quot;:{&quot;sid&quot;:&quot;(.*?)&quot;,.*?</li>'
		pattern = re.compile(patt_str,re.S)	
		songIds = re.findall(pattern,content)
		formdata = {"songIds":",".join(songIds)}
		#print formdata
		data_encoded = urllib.urlencode(formdata)
		#print data_encoded
	
		# 查询歌曲列表	
		songList = urllib2.urlopen(url_songs,data_encoded)
		songListJson = songList.read()
		#print songListJson
		song_dict = JSONDecoder().decode(songListJson)
		#print song_dict
		song_data_dict = song_dict.get('data').get('songList')
		#print song_data_dict 
		musicList = []
		for song_data in song_data_dict:
			#print song_data
			song_name = song_data.get('songName')
			song_artistName = song_data.get('artistName')
			song_format = song_data.get('format')
			song_link = song_data.get('songLink')
			song_description = u"我爱范晶"
			#print song_name+'--'+song_artistName+'.'+song_format+u'下载链接为：'+song_link
			#file = urllib.urlretrieve(song_link,"./songs/%s.mp3" % song_name)
			#print file 
			musicList.append([song_link,song_name,song_description])
		return musicList 
	except urllib2.URLError,e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason 

if __name__ == "__main__":
	print get_musiclist() 

