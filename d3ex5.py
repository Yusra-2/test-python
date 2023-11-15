PIN=1234
y=int(input ("enter your pin"))
balance=1000

if (PIN == y):
    x=int(input("enter the transfer amount"))
    xx= balance + x
    print("your bank account has", xx ,"$") 
else:
    print("your pin uncorrect")