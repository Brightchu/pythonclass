import webapp2

form="""
<form action="http://www.bing.com/search" >
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Bing" formtarget="_blank">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.write('Hello, World!')
		
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(form)

app = webapp2.WSGIApplication([('/', MainPage)], 
						      debug=True)

