hour=int(input("enter hour"))
minute=int(input("enter minute"))
t=input("am or pm")

hour2=int(input("enter hour"))
minute2=int(input("enter minute"))
t2=input("am or pm")

if(t == "am" and t2 == "pm"):
    print (hour, ":" , minute, t)
    
elif(t2 == "am" and t == "pm"):    
    print (hour2, ":" , minute2, t2)
    
else:
    if(hour<hour2):
        print(hour, ":" , minute, t)
        if(hour==hour2): 
            if(minute<=minute2): 
                print (hour, ":" , minute, t2)
            
    else:
        print (hour, ":" , minute, t)
