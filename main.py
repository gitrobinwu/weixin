#-*- coding:utf-8 -*- 
# filename: main.py
import web
from handle import Handle 

urls = (
	'/wx','Handle',
	'/(.*.mp3)','StaticFile'
)

class StaticFile:
	def GET(self,file):
		web.seeother('/static/'+file)

app = web.application(urls,globals())

if __name__ == '__main__':
	app.run()


