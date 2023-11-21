"""from math import *
nside=int(input("write num of side"))
side=float(input("write side"))

t=3.14
x= nside*(side**2)
y= 4*(tan(t/nside))
area= x/y
print("num of side =" , nside, "side =", side, "area=", area, "area=", round(area,2))

text=input("enter a text")
v= "auoie"
counter=0
def count_v (x):
    for y in x:
        if (text.upper() in v):
            
            
    return x
print(count_v(text))

#list exercise
list1= [11,8,5,4]
for i in range(len(list1)):
    print(i)


list1= [11,8,5,4]
for i in range(len(list1)):
    print(list1[i])
    
    
s="a b c"
li=s.split(" ")
print(li)

#using copy of a list
s=[11,8,5,4]
x= s.copy()
x[3] =12
print(s)
print(x)
    
x= [1,2,3]
for i in x:
    print(i, end=" ")
print("____")    
z= [1,2,3]
for j in z:
    print(j*2, end=" ")

count=0
z= [1,4,-1,-10]
for j in z:
    if (j <0):
        count +=1
        print(j, end=" ")
print()
print("you have",count, "negative num")

x= [-2,9,5,-5,1]
print(x[3])
print(xindex9(2))


n= [-2,9,5,-5,1]
n.remove(-5)
n.pop()
print(n)

#enter values and printthem in a list
result= []
while(True):
    y=input("enter num")
    if(y !="Q"):
        result+=y
    else:
        break
print(result)

#print num grater than 100 in the next position only
b= [100,201,99,101]
for i in b:
    if (i > 100):
        print(i, b.index(i))
        break"""

sides= [1,2,3,4,5,6]
counter= []
y= int(input("enter how many times you got each side: "))
def main():
    countInput()
    printCounter()
    
def countInput(sides):
    
def printCounter(counter):
    return countInput()
    print(sides, ":", counter, end="")

main()
