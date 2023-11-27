#the die game

def count_input(n):
    att=input("enter ur attempts: ").split(",")
    counter= []
    for i in range(1, n+1):
        counter.append(att.count(str(i)))
    return counter

def print_count(lst):
    for i in range(1, len(lst)+1):
        print("{} : {}".format(i, lst[i-1]))

def main():
    sides= int (input("enter a num of side"))
    clist= count_input(sides)
    print_count(clist)

main()