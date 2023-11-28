"""
#create a class
class Person:
    num_of_object =0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.num_of_object +=1
    def __str__(self):   
        return "hello {} you are {} years old".format(self.name, self.age)
person1= Person("ahmed", 27)
person2= Person("alla", 22)
person3= Person("alia", 29)
person4= Person("ali", 25)
print(person1.num_of_object)

#transfer obj from private to public
class Person:
    num_of_object =0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.num_of_object +=1
        #should use both get and set 
    def set_name(self, new_name):
        self.__name= new_name
    def get_name(self):
        return self.__name
    def __str__(self):   
        return "hello {} you are {} years old".format(self.__name, self.__age)
person1= Person("ahmed", 27)
person2= Person("alla", 22)
person3= Person("alia", 29)
person4= Person("ali", 25)
person3.set_name("sara")
print(person3)

#parent and child class
class Person:
    def __init__(self, name, age = 22, gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender
    def say_hi(self):
        print("hello {} from parent class, your age is {} and gender {}".format(self.name,self.age,self.gender))
class Student(Person):
    def __init__(self, name, age,gender="Male"):
        super().__init__(name,age, gender)
    def say_hi(self):
        print("hello {} from student, your age is {} and gender {}".format(self.name,self.age,self.gender))

p1= Person("A", 22)
p2= Student("B", 15, "female")
p3= Person("C", 25)
p4= Student("D", 4)
p1.say_hi()
p2.say_hi()
p3.say_hi()
p4.say_hi()    

#inheretence form parent class
from parent import *
def main():
    p1.say_hi()
    p2.say_hi()
    p3.say_hi()
    p4.say_hi()
    
main()
"""
# exercose
class Shape:
    def  __init__(self, name, color, description):
        self.name = name
        self.color= color
        self.description= description
        
    def Area():
        
        
        