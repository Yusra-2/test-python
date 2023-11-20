"""v="123456789"
counter=0
m=input("enter a text")
for chr1 in m:
    if chr1 in v:
        counter +=1
print (counter)"""
#num='+968'
#num[0] == '+'


while(True):
    x= "968"
    y=input("enter your number")
    if (len(y) ==11):
        if (y[:3]==x):
            if(y[3:].isdigit()):
                y1=y[3:7]
                y2=y[7:]
            print("+",x,y1,"-",y2)
            break
        else:
            print("enter the correct num")
    else:
        print("enter the correct country code")
else:
     print("enter the correct num")


    