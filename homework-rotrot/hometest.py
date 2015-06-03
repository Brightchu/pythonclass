# -*- coding: utf-8 -*- 
import webapp2
import cgi
import re

form="""
<form method="post" >
	<textarea name="text" style="height: 100px; width: 400px;">%(rottext)s</textarea>
	<br>	
	<input type="submit">
</form>
"""


# 用ord() chr() 来转换ASCII char
def rottransfer(rottext):
	rotted=""
	if rottext:
		for rotchar in rottext:
			if (ord(rotchar)>=65 and ord(rotchar)<=77) or (ord(rotchar)>=97 and ord(rotchar)<=109):
				rotchar=chr(ord(rotchar)+13)
			elif(ord(rotchar)>77 and ord(rotchar)<=90) or (ord(rotchar)>109 and ord(rotchar)<=122):
				rotchar=chr(ord(rotchar)-13)

			rotted=rotted+rotchar
	return rotted	
			

form2="""
<head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  <style type="text/css"></style></head>

 <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tbody><tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(error_username)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(error_pwd)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(error_pwd_v)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(error_email)s
          </td>
        </tr>
      </tbody></table>

      <input type="submit">
    </form>
  

</body>
"""


welcome="""
<h2>Welcome, %(username)s!</h2>
"""
def valid_name(username):
	error_username=""
	# using alnum to check whether the username is alphanumeric
	#if not username.isalnum():
		#error_username="That's not a valid username."
	username_p=re.compile(r"^[a-zA-Z0-9_-]{3,20}$",re.I)  # $ 确保完全匹配
	if not username_p.match(username):
		error_username="That's not a valid username."
	return error_username

def valid_email(email):
	error_email=""
	email_p=re.compile(r"^\S+@[a-zA-Z0-9_-]+\.\w+$",re.I)
	if not email_p.match(email) and email:
		error_email="That's not a valid email."
	return error_email

def valid_psw(password):
	error_pwd=""
	#pwd_p=re.compile(r"\S",re.I)
	if not (password and len(password)>2):
		error_pwd="That wasn't a valid password."
	return error_pwd

def psw_verify(password,verify):
	error_pwd_v=""
	if password!=verify:
		error_pwd_v="Your passwords didn't match."
	return error_pwd_v

class MainPage(webapp2.RequestHandler):
	def write_form(self,rottext=""): 
		self.response.out.write(form % {"rottext":cgi.escape(rottext,quote=True)})
		#self.response.out.write(form % {"rottext":rottext})

	def get(self):
		#self.response.write(form)
		self.write_form("")

	def post(self):
		user_rottext=self.request.get('text')
		self.write_form(rottransfer(user_rottext))

class SignUp(webapp2.RequestHandler):
	def write_form(self,username="",email="",error_username="",error_pwd="",error_pwd_v="",error_email=""): 
		self.response.out.write(form2 % {"error_username":error_username,
										"error_pwd":error_pwd,
										"error_pwd_v":error_pwd_v,
										"error_email":error_email,
										"username":cgi.escape(username,quote=True),
										"email":cgi.escape(email,quote=True)})


	def get(self):
		#self.response.out.write(form2)
		self.write_form("","","","","","")

	def post(self):
		username=self.request.get('username')
		#global glb_username                #不需要使用全局变量
		#glb_username=username
		password=self.request.get('password')
		verify=self.request.get('verify')
		email=self.request.get('email')
		error_username=valid_name(username)
		error_pwd=valid_psw(password)
		error_pwd_v=psw_verify(password,verify)
		error_email=valid_email(email)

		if not(error_email  or error_username or error_pwd or error_pwd_v):
			self.redirect("/welcome?username=%s" % username)
		else:
			self.write_form(username,email,error_username,error_pwd,error_pwd_v,error_email)

	

class WelcomePage(webapp2.RequestHandler):
	def write_form(self,username=""):
		self.response.out.write(welcome % {"username":cgi.escape(username,quote=True)})

	def get(self):
		username=self.request.get('username')
		self.write_form(username)
		#self.write_form(self.request.get('username'))
		
		#self.response.out.write(self.request)
		#self.response.out.write("glb_username=%s" % glb_username)
		#self.response.out.write(self.request.get('username'))


app = webapp2.WSGIApplication([('/', MainPage),
								('/signup',SignUp),
								('/welcome',WelcomePage)
								],
						      debug=True)   