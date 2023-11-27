"""def add_fun(x:int, y:int)->int:
    return x+y

z= add_fun(6,7)
print (z)
from typing import List

def reverse_list(li:List[int])->int:
    li.pop()
    return "hi"
    
li = [8,5,6,0,10]

print(li.reverse())

#fun+list
def readFloat(n):
    x= []
    for i in range(n):
        num= float(input("enter any num"))
        X.append(num)
    return x

def mulityply_(li, factor):
    for i in range(len(li)):
        li[i] = li[i]*factor
    return li
    
def printReverse():
    y= li.reverse()
    return y

def main():
    x= readFloat(3)
    num= int (input("enter factors: "))
    new_li= mulityply_(li, num)
    f_li= print_reverse(new_li)
    print(f_li)
    f_li= printReverse(mulityply_(readFloat(3),num))
    print(f_li)
#print(printReverse())

main()
    
#matrix exercise
matrix= [[0,5,1],
         [4,9,0],
         [0,6,0]]
count=0
#print(matrix[1][1])
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (matrix[i][j] ==0):
            count+=1
        #print(matrix end=" ")
print(count)

#matrix
m1=[[0,5,1],
    [4,9,0],
    [0,6,0]]

m2=[[5,5,1],
    [4,9,3],
    [2,6,1]]

def matrix_sm(m1,m2):
    nm =[]
    for row in range(len(m1)):
        rows =[]
        for cln in range(len(m1)):
            rows.append(m1[row][cln] + m2[row][cln])
        nm.append(rows)
    print(nm)
matrix_sm(m1, m2)

# matrix loop
rc= int(input("enter a number: "))
for i in range(rc):
    for j in range(rc):
        if (i == j):
            print (1, end=" ")
        else:
            print (0, end=" ")
    print()
    
# matrix loop as tringle    
rc= int(input("enter a number: "))
for i in range(rc):
    for j in range(rc):
        if (i <= j):
            print (1, end=" ")
        else:
            print (0, end=" ")
    print()
    
#dic
"ex1"
dic ={1:"x", 2:"y"}
print(dic.get(2,"w"))
for x in dic:
    print(x)
    
"ex2"   
print(dic.pop(2))
print(dic.values())

"ex3"
dic= {1:{"name":"Ali", "age": 24},
      2:{"name":"Alia", "age": 21}}
for x in dic:
    for y in dic[x]:
        print(dic[x][y])
"ex4"
dic= {1:{"name":"Ali", "age": 27, "sex": "M"},
      2:{"name":"Alia", "age": 22, "sex": "F"},
      3:{"name":"Alaa", "age": 23, "sex": "F"},
      4:{"name":"Ahmed", "age": 25, "sex": "M"}}

for i in dic:
    if(dic[i]["age"] > 22):
        print(dic[i]["name"])

#tuple
def fun1(t):
    t= t*2
t=(1,2,3)
print(t)
fun1(t)
print(t)"""
    
#set
ls= set([1,2,3,4])
ls.add(5)
ls.update("hi")
print(ls)

    
    