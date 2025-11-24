import copy

matrix = []
n = 0

while True:
    cmd = input().strip()
    if cmd == "stop":
        break

    elif cmd == "scan":
        n = int(input())
        matrix = [list(map(int, input().split())) for _ in range(n)]

    elif cmd == "rotate right":
        if not matrix:
            print("No element in matrix can be rotated.")
            continue
        new_matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n-1-i] = matrix[i][j]
        matrix = new_matrix

    elif cmd == "rotate left":
        if not matrix:
            print("No element in matrix can be rotated.")
            continue
        new_matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[n-1-j][i] = matrix[i][j]
        matrix = new_matrix

    elif cmd == "print":
        if not matrix:
            print("No element in matrix can be printed.")
            continue
        for i in range(n):
            print(" ".join(map(str, matrix[i])))


