"""ex3
sum1 = 0
for i in range(1, 101):
    for n in range(1, i): 
        if(i%n == 0):
            sum1 += n
    if(sum1 == i):
        print(i)
    sum1 = 0"""

#ex4
num= int(input("enter a num"))
n=len(num)
x= [num]**n
if (x==num):
    print("Yes")
else:
    print("No")



