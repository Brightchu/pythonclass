# -*- coding: utf-8 -*- 
import webapp2

# [GET]:添加最上面这一行就能支持中文了

form="""
<form action="http://www.bing.com/search" >
	<input name="q">
	<!-- submit and enter is the same -->
	<input type="submit" value="Bing一下" formtarget="_blank">
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

form3="""
<form method="post" action="/password" >
	<input type="password" name="q">
	<input type="submit" value="password" formtarget="_blank">
</form>
"""

form4="""
<form method="post" action="/validation" >
	What is your birthday? <br>
	<label>Month<input type="text" name="month"></label>
	<label>Day<input type="text" name="day"></label>
	<label>Year<input type="text" name="year"></label>
	<div style="color: red">%(error)s</div>  
	<br><br>
	<input type="submit"  formtarget="_blank">
</form>
"""

form5="""
<form method="post" >
	What is your birthday? <br>
	<label>Month<input type="text" name="month"></label>
	<label>Day<input type="text" name="day"></label>
	<label>Year<input type="text" name="year"></label>
	<div style="color: red">%(error)s</div>  
	<br><br>
	<input type="submit" >
</form>
"""

def valid_day(day):
	if day and day.isdigit():
		day=int(day)
		if day<32 and day>0:
			return day

def valid_year(year):
	if year and year.isdigit():
		year=int(year)
		if year<2050 and year>1900:
			return year			

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
		  
month_abbvs= dict((m[:3].lower(),m) for m in months )
		  
def valid_month(month):
	if month:
		short_month=month[:3].lower()
		return month_abbvs.get(short_month)
print valid_month("jan")
		  

class MainPage(webapp2.RequestHandler):
	def get(self):
		# self.response.headers['Content-Type'] = 'text/plain'
		# self.response.write('测试')
		
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(form)
		self.response.write(form1)
		self.response.write(form2)
		self.response.write(form3)
		self.response.write(form4)
		#self.response.write(valid_month("jan"))
		
		
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
		
class TestHandler3(webapp2.RequestHandler):
	def post(self):
		# q=self.request.get("q")
		# self.response.out.write(q+'<br>')  
		
		# [GET]:display http response
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request) 
		
class TestHandler4(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request) 
		
class TestHandler5(webapp2.RequestHandler):
	def write_form(self,error=""):   # take care here. the first parameter is 'self'
		self.response.out.write(form5 % {"error":error})  #advanced dictionary mapping string substitution  
	
	def get(self):
		self.write_form()
		
	def post(self):
		user_month=valid_month(self.request.get('month'))
		user_day=valid_day(self.request.get('day'))
		user_year=valid_year(self.request.get('year'))
		
		if (user_day and user_month and user_year):
			self.response.out.write("It's valid")
		else:
			mistake="month is %s, day is %s, year is %s " %(user_month, user_day, user_year)			
			self.write_form (mistake.replace("None","error")) #replace None with error for legibility
		
		
		
app = webapp2.WSGIApplication([('/', MainPage),
								('/testform', TestHandler),  # [GET]:add a new handler 
								('/testform2', TestHandler2),
								('/password', TestHandler3),
								('/validation', TestHandler4),
								('/valid', TestHandler5)
								],
						      debug=True)   
