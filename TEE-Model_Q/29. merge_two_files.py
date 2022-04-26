filenames = ['input.txt', 'myfile.txt']
  
with open('file3.txt', 'w') as outfile:
  
    for names in filenames:
  
        with open(names) as infile:
  
            outfile.write(infile.read())
  
        outfile.write("\n")

#https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/