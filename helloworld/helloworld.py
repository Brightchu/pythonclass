import webapp2

form=""""
<form action="http://www.google.com/search" target="_blank">
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Goolge">
</form>
""""

class MainPage(webapp2.RequestHandler):
	def get(self):
		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.write('Hello, World!')
		
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(form)

app = webapp2.WSGIApplication([('/', MainPage)], 
						      debug=True)

