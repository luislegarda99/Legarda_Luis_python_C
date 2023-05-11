
A=[[1,2,3],[4,5,6]]
B=[[-1,0],[0,1],[1,1]]

C=[]
for i in range(0,2):
    row=[]        
    for j in range(0,2):
        number=0
        for k in range(0,3):
            pp=A[i][k]*B[k][j]
            number+=pp
        row.append(number)
    C.append(row)
print(C)