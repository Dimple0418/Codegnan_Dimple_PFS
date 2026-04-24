'''

class student:
    def __init__(self,Student_name,Education,Roll_no,Course):
        self.Student_name=Student_name
        self.Education=Education
        self.Roll_no=Roll_no
        self.Course=Course
    def display(self):
        print("----------------------------------------")
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
    
    
some1 = student("S.Raghu","B.TECH",2005,"Python")
some1.display()
print("----------------------------")
some2 = Professor("Bhanu teja", 123 , "Python")
some2.display()
print("---------")


'''


# LMS PORTAL USING OOP CONCEPTS

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def display_info(self):
        print("User Name:", self.name)
        print("User ID:", self.user_id)


class Student(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.__courses = []   # Encapsulation (private)

    def enroll_course(self, course):
        self.__courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")

    def show_courses(self):
        print(f"Courses enrolled by {self.name}:")
        if len(self.__courses) == 0:
            print("No courses enrolled")
        else:
            for c in self.__courses:
                print("-", c.course_name)

    def display_info(self):   # Polymorphism (Overriding)
        print("\n--- Student Details ---")
        print("Student Name:", self.name)
        print("Student ID:", self.user_id)


class Instructor(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def display_info(self):   # Polymorphism (Overriding)
        print("\n--- Instructor Details ---")
        print("Instructor Name:", self.name)
        print("Instructor ID:", self.user_id)


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def show_course(self):
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)


class LMS:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        print("Student Added Successfully!")

    def add_course(self, course):
        self.courses.append(course)
        print("Course Added Successfully!")

    def show_all_students(self):
        print("\n--- All Students ---")
        if len(self.students) == 0:
            print("No students available")
        else:
            for s in self.students:
                print(f"{s.user_id} - {s.name}")

    def show_all_courses(self):
        print("\n--- All Courses ---")
        if len(self.courses) == 0:
            print("No courses available")
        else:
            for c in self.courses:
                print(f"{c.course_id} - {c.course_name}")

    def enroll_student(self, student_id, course_id):
        student = None
        course = None

        for s in self.students:
            if s.user_id == student_id:
                student = s
                break

        for c in self.courses:
            if c.course_id == course_id:
                course = c
                break

        if student and course:
            student.enroll_course(course)
        else:
            print("Invalid Student ID or Course ID")


# ---------------- MAIN PROGRAM ----------------

lms = LMS()

while True:
    print("\n====== LMS PORTAL MENU ======")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Show All Students")
    print("5. Show All Courses")
    print("6. Show Student Courses")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        sid = int(input("Enter student id: "))
        student = Student(name, sid)
        lms.add_student(student)

    elif choice == 2:
        cid = int(input("Enter course id: "))
        cname = input("Enter course name: ")
        course = Course(cid, cname)
        lms.add_course(course)

    elif choice == 3:
        sid = int(input("Enter student id: "))
        cid = int(input("Enter course id: "))
        lms.enroll_student(sid, cid)

    elif choice == 4:
        lms.show_all_students()

    elif choice == 5:
        lms.show_all_courses()

    elif choice == 6:
        sid = int(input("Enter student id: "))
        found = False
        for s in lms.students:
            if s.user_id == sid:
                s.show_courses()
                found = True
                break
        if not found:
            print("Student not found")

    elif choice == 7:
        print("Exiting LMS Portal...")
        break

    else:
        print("Invalid choice")







