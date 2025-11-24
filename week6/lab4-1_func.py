def countCarry(a, b):
    num1 = list(a)
    num2 = list(b)

    while len(num1) < len(num2): 
        num1.insert(0, '0')
    while len(num2) < len(num1):
        num2.insert(0, '0')

    plusNum = -1
    carry = 0
    count = 0

    while abs(plusNum) <= len(num1):
        if (int(num1[plusNum]) + int(num2[plusNum]) + carry) >= 10:
            carry = 1
            count += 1
        else:
            carry = 0
        plusNum -= 1

        if abs(plusNum) > len(num1):
            break

    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.") 
    else:
        print(f"{count} carry operations.")


def main():
    while True:
        a, b = input().split()
        if a == "0" and b == "0":
            break
        countCarry(a, b)

main()