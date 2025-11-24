height = int(input(""))

if(height > 1):
    for j in range(height):
        for k in range(2*height-1):
            if(j == abs(height-1-k)):
                print("*",end="")
            else:
                if(j == height-1):
                    print("*",end="")
                else:
                    print(" ",end="")
        print("")
else:
    print("輸入錯誤")