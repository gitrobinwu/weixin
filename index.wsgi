import sae
from webpy import app
application = sae.create_wsgi_app(app.wsgifunc())


