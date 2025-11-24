n = int(input())
for _ in range(n):
    counter = {}
    line = input()
    for char in line:
        counter[char] = counter.get(char, 0) + 1
    max_value = max(counter.values())
    for k, v in counter.items():
        if v == max_value:
            print(k)
            break 