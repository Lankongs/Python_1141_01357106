N = 1

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a



while(True):
    N = int(input())
    G = 0
    if(N == 0):
        break
    for i in range(1,N):
        for j in range(i+1,N+1):
            G += GCD(i,j)
    print(G)