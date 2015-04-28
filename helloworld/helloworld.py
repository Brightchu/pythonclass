# -*- coding: utf-8 -*- 
import webapp2

# [GET]:添加最上面这一行就能支持中文了

form1="""
<form action="http://www.bing.com/search" >
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Bing" formtarget="_blank">
</form>
"""
form2="""
<form action="/testform" >
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Testform2" formtarget="_blank">
</form>
"""


class MainPage(webapp2.RequestHandler):
	def get(self):
		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.write('测试')
		
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(form2)
		
class TestHandler(webapp2.RequestHandler):
	def get(self):
		# q=self.request.get("q")
		# self.response.out.write(q+'<br>')  
		
		# [GET]:display http response
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)                  
		
app = webapp2.WSGIApplication([('/', MainPage),
								('/testform', TestHandler)],  # [GET]:add a new handler 
						      debug=True)   
