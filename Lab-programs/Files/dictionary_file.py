
details={'Name' : "Varun",
         'Age' : 19,
         'Degree' : "B.Tech CSE Core",
         'University' : "VIT Bhopal"}
  
with open("myfile.txt", 'w') as f: 
    for key, value in details.items(): 
        f.write('%s:%s\n' % (key, value))