import copy
n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

commands = input()
for command in commands:
    if command == "R":
        old_matrix = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = old_matrix[i][j]
    elif command == "H":
        for i in range(n):
            matrix[i] = list(reversed(matrix[i]))
    elif command == "V":
        for i in range(n):
            for j in range(n//2):
                temp = matrix[j][i]
                matrix[j][i] = matrix[n-j-1][i]
                matrix[n-j-1][i] = temp

for i in range(n):
    if(i != 0):
        print()
    for j in range(n):
        if(j == n):
            print(matrix[i][j],end="")
        else:
            print(f"{matrix[i][j]} ",end="")

