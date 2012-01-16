
from google.appengine.ext import webapp
from google.appengine.ext.ndb import context
import jinja2
import os

debug = True

current_dir = os.path.dirname(__file__)
current_path = os.path.abspath(current_dir)

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(current_dir, 'templates')))
jinja_environment.globals.update(dict(
    app_version = os.environ['CURRENT_VERSION_ID']
))

def render(template_file, data = {}):
    template = jinja_environment.get_template(template_file)
    response = webapp.get_request().app.response_class()
    response.out.write(template.render(data, url_for = webapp.uri_for))
    return response

def home(request):
	return render('home.html')

def faq(request):
	return render('faq.html')

ROUTES = [
	webapp.Route('/faq', handler=faq, name='faq'),
	webapp.Route('/', handler=home, name='home')
]

application = webapp.WSGIApplication(ROUTES, debug=debug)
application = context.toplevel(application.__call__)

