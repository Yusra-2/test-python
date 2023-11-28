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
# shapes exercise
class Shape:
    def  __init__(self,color, name):
        self.color= color
        self.name = name
    def __str__(self):   
        return "hello your shape is {} {} ".format(self.color,self.name)    

class Circle(Shape):
    def  __init__(self,color, name, r):
        super().__init__(color, name)
        self.r= r
    def Carea(self):
        aoc= (3.14*(self.r**2))      
        return aoc      
    def __str__(self):   
        return "hello your shape is {} {} and the radius = {}".format(self.name, self.color, self.r)

class Square(Shape):    
    def  __init__(self,color, name, length):
         super().__init__(color, name)
         self.length= length
    def Sarea(self):   
        aos= (self.length**2)
        return aos
    def __str__(self):   
        return "hello your shape is {} {} and the length = {}".format(self.color, self.name, self.length)
                   
                   
c1= Circle("red","circle", 10)
c2= Circle("blue","circle", 10)
s1= Square("yellow","square", 5)
s2= Square("green","square", 2)

print(c1)
print("the area =", int(c1.Carea()))
print(c2)
print("the area =", int(c2.Carea()))
print(s1)
print("the area =", int(s1.Sarea()))
print(s2)
print("the area =", int(s2.Sarea()))