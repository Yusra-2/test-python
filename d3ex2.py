y= int(input ("enter the total price"))
if (y >= 100):
    print("you will get 10% discount")
    d= (y - (y*10/100))
    print(("total price with discount is "), d)
else:
    print("you will get 5% discount")
    d= (y - (y*5/100))
    print(("total price with discount is "), d)