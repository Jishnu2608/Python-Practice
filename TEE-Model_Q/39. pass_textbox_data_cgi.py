import cgi, cgitb
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered"
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Textbox CGI program</title>")
print ("</head>")
print ("<body>")
print ("<h2> Entered Text Content is %s</h2>" % text_content)
print ("</body>")