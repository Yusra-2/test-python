"""n=5
result=1
for i in range(1,1+n):
    if(i !=n):
        print(i, end="x")
    else:
        print(i)
    result*=i
print(result)

#same example using while
i=1
while(i<=n):
    if(i !=n):
        print(i, end="x")
    else:
        print(i)
    result*=i
    i +=1
print(result)


#exercise
n= 4
sm=0

result=0
for i in range (1, n+1):
    result = "2"*i
    sm +=int(result)
    print(result)
print(sm)

#create and call function
def sum_num(*args):
    sm=0
    for n in args:
        sm +=n
    return sm
result= sum_num(1,3,4)
print(result)

#using main function to call 2 created functions
num=5
def main():
    print(func1(2), func2(1))
    
def func1(x):
    return x*num
    
def func2(x):
    i=4
    y=3
    return i*x+y-num

main()"""

#create a function 
def sum_num(x):
    sm=0
    while(x !=0):
        sm +=x%10
        x=x//10
    print(sm)
sum_num(234)


    

   