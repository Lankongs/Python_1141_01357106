def isPossible(target):
    stack = []
    current = 1
    max_num = max(target)

    for num in target:
        while current <= max_num and (not stack or stack[-1] != num): 
            stack.append(current)
            current += 1
        if stack[-1] == num:
            stack.pop()
        else:
            return False
    return True

results = []
n = input()

while True:
    line = input()
    if line.strip() == "0":
        break
    nums = list(map(int, line.split()))
    if isPossible(nums):
        results.append("YES")
    else:
        results.append("NO")

for res in results:
    print(res)