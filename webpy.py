import web 

urls =(
    '/.*','hello',
    '/world',"world",
)

class hello:
	def GET(self):
		web.header('Content-Type', 'text/html; charset=UTF-8')
		return "hello, world,This is a Test!"

class world:
    def GET(self):
        web.header('Content-Type','text/html; charset=UTF-8')
        return "111111111111111111!"
    
app = web.application(urls,globals())
if __name__ == '__main__':
	app.run() 




