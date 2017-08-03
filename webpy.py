import web 

urls =('/.*','hello')

class hello:
	def GET(self):
		web.header('Content-Type', 'text/html; charset=UTF-8')
		return "hello, world!"

app = web.application(urls,globals())
if __name__ == '__main__':
	app.run() 




