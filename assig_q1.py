#answer of q1
x=float(input("enter rockwell hardness="))
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
    
#answer of q3