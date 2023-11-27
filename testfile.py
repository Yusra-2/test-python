"""
#read from external file
f= open("test.txt", "r")
l= f.readline()
print(l)

while (l != ""):
    l= f.readline()
    print(l)

#read from external+ count avrage
f= open("test.txt", "r")
l= f.readline()
sm= 0
count= 0
for l in f:   
    sm += float(l)
    count+=1
print(sm/count)

#write in file
f= open("test.txt", "w")
print("hello python", file= f)
f.close()

#read and split from file
f= open("test.txt", "r")
for line in f:
    line= line.rsplit(" ")
    print(line)
"""
