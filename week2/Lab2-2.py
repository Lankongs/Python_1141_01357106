n = int(input("請輸入 n:"))
l1 = list(map(int, input("請輸入數列:").split()))

print("排序前的數列 :",end="")
for j in range(n):
    print(l1[j],"",end="")
print("")

for j in range(len(l1)-1):
    for k in range(len(l1)-1):
        if (l1[k] > l1[k+1]):
            temp = l1[k]
            l1[k] = l1[k+1]
            l1[k+1] = temp

    

print("排序後的數列: ",end="")
for j in range(n):
    print(l1[j],"",end="")