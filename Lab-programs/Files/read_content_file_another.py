file= open("input.txt","w") 
file.write("""This is an input file. 
Greetings people. 
Adios amigo !""")
file.close()

with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        for line in input:
            output.write(line)
