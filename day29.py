class student:
    def __init__(self,Student_name,Education,Roll_no,Course):
        self.Student_name=Student_name
        self.Education=Education
        self.Roll_no=Roll_no
        self.Course=Course
    def display(self):
        print(f"STUDENT NAME : {self.Student_name}")
        print(f"EDUCATION: {self.Education}")
        print(f"STUDENT ROLL NO : {self.Roll_no}")
        print(f"COURSE : {self.Course}")
                
class Professor(student):
    def __init__(self,Professor_name,Employee_id,Course):
        self.Professor_name=Professor_name
        self.Employee_id=Employee_id
        self.Course=Course
    def display(self):
        print(f"PROFESSOR NAME : {self.Professor_name}")
        print(f"EMPLOYEE ID :{self.Employee_id}")
        print(f"COURSE : {self.Course}")
    
    
some1 = student("Ch.Dimple","B.TECH",2005,"Python")
some1.display()
print("----------------------------")
some2 = Professor("Bhanu teja", 123 , "Python")
some2.display()
print("---------")















