year=int (input ("enter any year:"))
if ((year %  400 == 0)and(year %  100 == 0)):
    print("is a leap year")
elif((year %  4 == 0)and(year %  100 != 0)):
    print("is a leap year")
else:
    print("is not a leap year")