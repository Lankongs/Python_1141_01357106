def buyCola(n):
    colas = 0
    empty = n

    while empty >= 3:
        new = empty // 3
        colas += new
        empty = empty % 3 + new

    if empty == 2:
        colas += 1

    print(colas + n) 

while True:
    try:
        n = int(input())
        buyCola(n)
    except EOFError:
        break
