nums = []

try:
    while True:
        x = int(input())  
        nums.append(x)  
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        if n % 2 == 1:  
            median = nums[n // 2]
        else:         
            median = (nums[n // 2 - 1] + nums[n // 2]) // 2

        print(median)

except EOFError:
    pass