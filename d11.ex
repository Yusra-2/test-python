"""
# creating Employee class
class Employee:
    def __init__(self,name, ID, dep, salary, h):
        self.name = name
        self.ID = ID
        self.dep= dep
        self.salary = salary
        self.h = h
    
    def assign_dep(self,new_dep):
        self.dep= new_dep
    def cal_emp_sa(self):
            if(self.h > 50):
                ov= self.h - 50
                ov_amount= (ov* self.salary /50)
                new_sal= self.salary + ov_amount
                return new_sal
    def say_hi(self):
        print("hello {} your ID {} from {} your salary is {}".format(self.name,self.ID,self.dep, self.salary))    
        
e1= Employee("Ahmed","E7880","HR",50000, 50)
e2= Employee("Walead","E6420","Sale",45000, 60)
e3= Employee("Adam","E8802","Account",50000, 55)
e4= Employee("Omar","E2256","IT",55000, 65)

#to change e1 dep
e1.assign_dep("PR")

e1.say_hi()
e2.say_hi()
print("your salary will be", int(e2.cal_emp_sa()))
e3.say_hi()
print("your salary will be", int(e3.cal_emp_sa()))
e4.say_hi()
print("your salary will be", int(e4.cal_emp_sa()))


#creating a class and add numbers
class Numbers:
    def __init__(self):
        self.numbers= []
        
    def add_num(self, num):
        self.numbers.append(num)
        
    def Sum_num(self):
        sm= 0
        for i in self.numbers:
            sm += i
        return sm
    
n1= Numbers()
n1.add_num(2)
n1.add_num(3)
print(n1.Sum_num())

#exercise 1: creating a bank class
class BankAccount:
    def __init__(self, acc_num, balance):
        self.__acc_num= acc_num
        self.__balance= balance
        
    def Deposit(self, amount):
        self.__amount= amount
        new_balance= (self.__balance + self.__amount)
        return new_balance
    def Withdrawal(self, wt):
        self.__wt= wt
        new_balance2= (self.__balance - self.__wt)
        return new_balance2
    def Display(self):
        print("Account number {} has {}".format(self.__acc_num, self.__balance))
        
a1= BankAccount(100455946002105, 100)
a1.Display()      
print("your balance:", a1.Deposit(150))
print("your balance has:",a1.Withdrawal(20))

#exercise2: add an exception (error)
#creating a bank class
class BankAccount:
    def __init__(self, acc_num, balance):
        self.__acc_num= acc_num
        self.__balance= balance
        
    def Deposit(self, amount):
        self.__amount= amount
        new_balance= (self.__balance + self.__amount)
        return new_balance
    def Withdrawal(self, wt):
        try:
            self.__wt= wt
            if (self.__wt > 0):
                new_balance2= (self.__balance - self.__wt)
                return new_balance2
            else:
                print("please enter the correct amount")
        except Exception as exc:
            print("error: ",str(exc))
        
    def Display(self):
        print("Account number {} has {}".format(self.__acc_num, self.__balance))
        
a1= BankAccount(100455946002105, 100)
a1.Display()      
print("your balance:", a1.Deposit(150))
print("your balance has:",a1.Withdrawal("a"))

"""        
              
# exercise 3: creating a library
class Library:
    def __init__(self):
        self.library= []
        
    def add_book(self, title, author, copies):
        book= {"Title":title,"Author":author,"Copies":copies}
        self.library.append(book)

    def disply_book(self):
        for i in self.library:
            print(i)
        
    def ser_book(self, title):
       for i in self.library:
           if (i["Title"] == title):
                print(i) 
        
b1= Library()
b1.add_book("Python","A",4)
b1.add_book("C++","B",2)
#b1.disply_book()
x= input("enter the title of the book")
b1.ser_book(x)


