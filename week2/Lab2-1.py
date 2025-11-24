height = int(input("請輸入矩陣高度:"))
number = 1
n = 0

for j in range(height+1):
    for k in range(j):
        n+=1
print(n)
if(height > 0):
    for j in range(height+1):
        for k in range(j):
            numstr = str(number)
            aligned = numstr.rjust(len(str(n)))
            print(f"{aligned}",end=" ")
            number += 1
        print("")
else:
    print("輸入錯誤")