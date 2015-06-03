import os
import webapp2

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

class MainPage(Handler):
	def get(self):
		self.write(form_html)


app=webapp2.WSGIApplication([('/',MainPage)
							 ],
							 debug=True)