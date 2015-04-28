# -*- coding: utf-8 -*- 
import webapp2

# [GET]:添加最上面这一行就能支持中文了

form="""
<form action="http://www.bing.com/search" >
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Bing" formtarget="_blank">
</form>
"""
form1="""
<form action="/testform" >
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Testform1" formtarget="_blank">
</form>
"""

#[GET]: the default method is "get", 
form2="""
<form method="post" action="/testform2" >
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
		self.response.write(form)
		self.response.write(form1)
		self.response.write(form2)
		
class TestHandler(webapp2.RequestHandler):
	def get(self):
		# q=self.request.get("q")
		# self.response.out.write(q+'<br>')  
		
		# [GET]:display http response
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request) 
		
class TestHandler2(webapp2.RequestHandler):
	def post(self):
		q=self.request.get("q")
		self.response.out.write(q+'<br>')    # [GET]: 当使用post时，URL里面不会出现 "?q=..."的值
		
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request) #[GET]: "get" 将参数加进了URL, POST将参数加进 request body 中
		
  		
		
app = webapp2.WSGIApplication([('/', MainPage),
								('/testform', TestHandler),  # [GET]:add a new handler 
								('/testform2', TestHandler2)],
						      debug=True)   
