"""
#answer q1
values= [0,0,0,0,0,0,0]
values[0]= 10
values[6]= 10
print(values)

#answer q2
li= [6,3,8,1,7]
rev= li[::-1]
print(rev)

#answer q3
li= ["red", "yellow", "pink", "black"]
print(li)
li.insert(1,"purple")
li.remove("pink")
li.append("green")
print(li)

#answer q4
fruit = ["orane", "apple", "pear", "banana", "kiwi", "apple", "banana"]
a= fruit.count("apple")
print(a)
v= fruit.count("struberry")
print(v)
n= fruit.index("banana")
print(n)
m= fruit.index("banana", 4)
print(m)
fruit.reverse()
print(fruit)
fruit.append("grape")
print(fruit)
fruit.sort()
print(fruit)
fruit.pop()
print(fruit)

#answer q5
y= [23,54,76,12,90]
for i in range(len(y)):
    if (i !=4):
        print(y[i], end="|")
    else:
        print(y[i], end=" ")

#answer q6
li=[0,1,0,5,8,0,0,2,]
for i in li:
    x= li.count(0)
print(x)

#answer q7
d= "a*hj"
list(d)
print(list(d))

#answer q8
b= ["p","r","a","c","t","i","c","e"]
for i in b:
    print(i, end="?")
    
#answer q9
b= "Hello World"
a= list(b)
print(a)
print(len(a))
print(a[1:11])
print(a[-2:-5:-1])
print(a[::2])
print(a[:4])
print(a[4:])
"""
#answer q10
import random
def find_length(word,n):
    li=[]
    for text in word:
        if len(text)>n:
            li.append(text)
    return li
n= int(input("enter the length"))
word=("words", "text","message", "sentence", "hi1world33")
x= random.choice(word)
print("the chosen word is: ", x)

y= find_length(word,n)
print(y)


