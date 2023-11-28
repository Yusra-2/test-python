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
  


