import cgi, cgitb

form = cgi.FieldStorage()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Checkbox CGI program</title>")
print("</head>")
print("<body>")
print('<form action = "\example\\38. pass_checkbox_data_cgi.py" method = "POST" target = "_blank">')
print('<input type = "checkbox" name = "maths" value = "on"> Maths')
print('<input type = "checkbox" name = "physics" value = "on"> Physics')
print("</form>")
print("<body>""</body>")
print("</html>")

if form.getvalue("maths"):
    math_flag = "ON"
else:
    math_flag = "OFF"
if form.getvalue("physics"):
    physcis_flag = "ON"
else:
    physics_flag = "OFF"
print("<h2> Checkbox Maths is: %s</h2>" %math_flag)

print("<h2> Checkbox Physics is: %s</h2>" %physics_flag)
