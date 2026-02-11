##Write a python program Create an abstract class Student with a method calculate_grade(). Subclasses: UGStudent(marks) should
##return: A if marks > 90 ,B if marks > 75 .C if marks > 60 , F otherwise; PGStudent(marks) should return: A if marks > 85 ,B if
##marks > 70 ,C if marks > 50 ,F otherwise Input Format : First line: Type of student (UG or PG) and Second line: Marks (an integer)
##Output Format : Print the grade as A, B, C, or F
'''from abc import ABC,abstractmethod

class Student(ABC):
    @abstractmethod
    def calculate_grade(self,marks):
        pass
class UGStudent(Student):
    def calculate_grade(self,marks):
        if marks > 90:
            return 'A'
        elif marks > 75:
            return 'B'
        elif marks > 60:
            return 'C'  
        else:
            return 'F'

class PGStudent(Student):
    def calculate_grade(self,marks):
        if marks > 85:
            return 'A'
        elif marks > 70:
            return 'B'
        elif marks > 50:
            return 'C'
        else:
            return 'F'

stype=input("Student: ")
marks=int(input("Marks: "))


if stype == "UG":
    obj=UGStudent()
    print("Grade:",obj.calculate_grade(marks))
elif stype == "PG":
    obj=PGStudent()
    print("Grade:",obj.calculate_grade(marks))
else:
    print("Invalid option")'''

##Write a python program to Create an abstract class UserAuth with a method login(). Subclasses Admin and Guest should
##implement the login() method and return:"Admin login successful" for Admin and "Guest login successful" for Guest .Do not use
##abc or any external module. Input Format : A single line containing either "Admin" or "Guest" Output Format : Print the result of
##the login() method. otherwise to prints "invalid user login"
'''class UserAuth():
    def login(self,User):
        # This acts like an abstract method (manual abstraction)
        raise NotImplementedError("Subclass must implement login()")
class Admin(UserAuth):
    def login(self,User):
        return "Admin login Successful"
class Guest(UserAuth):
    def login(self,User):
        return "Guest login Successful"

User = input("User:")

if User == "Admin":
    obj=Admin()
    print("User:",obj.login(User))
elif User == "Guest":
    obj=Guest()
    print("User:",obj.login(User))
else:
    print("Invalid user login")'''















