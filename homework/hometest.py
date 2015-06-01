# -*- coding: utf-8 -*- 
import webapp2
import cgi

form="""
<form method="post" >
	<textarea name="test" style="height: 100px; width: 400px;">%(rottext)s</textarea>
	<br>	
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self,rottext=""): 
		self.response.out.write(form % {"rottext":rottext})

	def get(self):
		self.response.write(form)

	def post(self):
		user_rottext=self.request.get("rottext")
		self.write_form(user_rottext)



app = webapp2.WSGIApplication([('/', MainPage),],
						      debug=True)   