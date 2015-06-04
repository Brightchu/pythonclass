# -*- coding: utf-8 -*- 
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
<input type="text" name="food">
<input type="hidden" name="food" value="eggs">
<button>Add</button>
</form>
"""

class Handler(webapp2.RequestHandler):   
	def write(self, *a, **kw):    #
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Test(Handler):
	def get(self):
		#self.write(form_html)
		##name=self.request.get_all("food")           #get_all function 获得所有的参数，并写到list里面
		n=self.request.get("n",0)		#set the default value 设置初始值
		# if not n:						#set the default value 设置初始值
		# 	n=0
		self.render("test.html", n=int(n))
		#self.render("shopping_list.html",name=self.request.get("name"))

class MainPage(Handler):
	def get(self):
		items=self.request.get_all("food")		 #get_all function 获得所有的参数，并写到list里面
		self.render("shopping_list.html",items = items)
		


app=webapp2.WSGIApplication([('/',MainPage),
							 ('/jinjatest',Test)
							 ],
							 debug=True)