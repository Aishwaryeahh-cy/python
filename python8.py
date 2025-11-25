# Day 8 of practicing python
class Student:
    name="ashley"
s1 = Student()
print(s1.name) 
class Car:
    color="blue"
car1 = Car()
print(car1.color)
class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("Adding new student in Database..")
s1=Student("ash")
print(s1.name)        
s2=Student("aman")
print(s2.name) 