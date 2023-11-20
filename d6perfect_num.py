#n= 6
sum1=0
for num in range(1,101):
    for i in range(1,num):
        if(num%i ==0):
            #print(i, end="")
            sum1 +=i
    
#print("\n",sum1)
    if(sum1 == num):
        print(num, "is a prfect number")
    sum1=0
