A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
C = []

for i in range(len(A)):
    C.append([])
    for j in range(len(B[i])):
        element = 0
        for k in range(len(B)):
         element += A[i][k]*B[k][j]
        C[i].append(element)
print(C)
