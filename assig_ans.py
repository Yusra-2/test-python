#answer of q1 
"""x=float(input("enter rockwell hardness="))
y=float(input("enter carbon content="))
z=float(input("enter tensile strength="))

if (x >=50 and y >=0.7 and z >=5600):
    print("grade 10")
elif (x >=50 and y >=0.7):
    print("grade 9")
elif (y >=0.7 and z >=5600):
    print("grade 8")
elif (x >=50 and z >=5600):
    print("grade 7")
else:
    print("grade 0")
    
#answer of q2
c= 10000
i= .05
y= 10
x=0
y1= 1
while (y1 <=y):
    c= c*(1+i)
    print("tuition in a year " + str(y1) +": "+str(c)+ " $")
    if (y1 <=4):
        x +=c
    y1 +=1
print("total cost in 4 years= "+str(x)+ " $")"""
        
#answer of q3
rows = 8
for i in range(1, rows+1):
    for space in range(rows,i,-1):
        print("  ", end="  ")
        #count+=1
    for space in range(1,i+1):
        y=2**(space-1)
        print(y, end="  ")
    for space in range(i-1,0,-1):
        y=2**(space-1)
        print(y, end="  ")
    print()
  
