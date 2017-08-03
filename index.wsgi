import web 
urls = (
	"/(.*)","index",
)

class index:
	def GET(self):
		web.header('Content-Type','text/html;charset=UTF-8')
		return "hello world,This is A Test!"

app = web.application(urls,globals())


import sae
application = sae.create_wsgi_app(app.wsgifunc())



