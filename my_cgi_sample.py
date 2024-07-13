import cgi.cgitb
form=cgi.FieldStorage()
firstname=form.getvalues("FirstName")
lastname=form.getvalues("Lastname")
print ("Content-type:text/html\r\n\r\n")
print("<HTML>")
print("<HEAD>")
print("<title>hello</title>")
print("<h2>welcome %s %s</h2>" % (firstname,lastname))
print("</HEAD>")
print("<HTML>")



