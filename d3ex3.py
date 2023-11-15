g=input("enter your gender, f or m")
if (g=="m"):
    age=int(input("enter your age"))
    if(age>=24 and age<=30):
        print("accepted")
    else:
        print("rejected")
else:
    print("rejected")
        