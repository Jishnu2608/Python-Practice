class Classroom:
    clscount = 0
    def __init__(self,name,course_name):
        self.name = name
        self.course_name = course_name
        Classroom.clscount +=1
    
    def displayCount(self):
     print ("Total Students %d" % Classroom.clscount)
    
    def displayStudent(self):
        print ("Name : ", self.name,  ", Course name: ", self.course_name)
    
cls1=Classroom("Varun","CSE3004")
cls2=Classroom("Abhay","CSE2001")
cls3=Classroom("Jishnu","MAT1001")
    
cls1.displayStudent()
cls2.displayStudent()
cls3.displayStudent()

print ("Total Students: %d" % Classroom.clscount)
    
    