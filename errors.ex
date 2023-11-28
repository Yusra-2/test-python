"""
#error & except 
try:
    x= 4/0
    print(x)
except:
    print("you can't divide by 0")
 
#usring exception framework
try:
    x= 4/6
    print(y) 
except ZeroDivisionError:
    print("you can't divide by 0")
except Exception as exc:
    print("error: ",str(exc))

#usring exception framework
try:
    x= [6,2,5,7,2]
    print(x[2])
except ZeroDivisionError:
    print("you can't divide by 0")
except IOError:
    print("...")
except Exception as exc:
    print("error: ",str(exc))
finally:
    print("done")

#exercise
try:
    x= float(input("enter a num"))
    print(int(x))
except Exception as exc:
    print("error: ",str(exc))

"""