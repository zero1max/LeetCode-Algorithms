nums = [2,7,11,15]
target = 9

result = []
for i in range(len(nums)):
    for x in range(i+1, len(nums)):
        if nums[i] + nums[x] == target:
            result = [i, x]
            print(result)