"""x= [1,3,2,4]
y= [i*10 for i in x]
print(y)"""

#matrix*matrix
mt1= [[1,2,3],
     [6,7,8]]

mt2= [[6,1],
     [2,10],
     [0,2]]
def multi_matrix(m1,m2):
    m3= [[0,0],[0,0]]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j]+=m1[i][k]*m2[k][j]
    return m3
print(multi_matrix(mt1,mt2))

