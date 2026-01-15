# class Student:
#     def __init__(self,name):
#         self.name = name
# s1= Student("Aishwarya")
# print(s1.name)
# del s1.name
# print(s1.name)
class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def start():
        print("car stopped...")
class Toyoto(car):
      def __init__(self,name):
        self.name=name    
car1 = Toyoto("fortuner")
car2 = Toyoto("plus")    
print(car1.start())             
