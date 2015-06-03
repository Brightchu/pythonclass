import os
import webapp2
import jinja2

#jinja template initialization
template_dir = os.path.join(os.path.dirname(__file__), 'templates') #set the template directory
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), #initial the jinja2
                               autoescape = True)

form_html="""
<form>
<h2>Add a food</h2>
<input type="text" name=food></input>
<input type="hidden" name=food value="eggs"></input>
<button>Add</button>
</form>
"""

class Handler(webapp2.RequestHandler):    #define a new cal
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	def render_str(self,template, **params):
   		t = jinja_env.get_template(template)
    	return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		self.write(form_html)


app=webapp2.WSGIApplication([('/',MainPage)
							 ],
							 debug=True)