def program9():
    f = open("input.txt","r")
    print(f.tell())
    f.seek(4,0)
    print(f.read(5))
    f.seek(10,0)
program9()

#https://www.tutorialaicsip.com/cs-xii-pra/python-file-handling-programs/