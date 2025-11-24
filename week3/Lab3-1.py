n, m = map(int, input().split())

Afriends = set(map(int, input().split()))
Bfriends = set(map(int, input().split()))

common = sorted(Afriends & Bfriends)
print(len(common))
if common:
    print(" ".join(map(str,common)))
