def sortArray(nums):
    if len(nums) == 1:
        return nums
    sorted1 = sortArray(nums[0: len(nums)//2])
    sorted2 = sortArray(nums[len(nums)//2:])
    res = []
    i = j = 0
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] <= sorted2[j]:
            res.append(sorted1[i])
            i += 1
        else:
            res.append(sorted2[j])
            j += 1
    if i < len(sorted1):
        for k in range(i, len(sorted1)):
            res.append(sorted1[i])
    elif j < len(sorted2) :
        for k in range(j, len(sorted2)):
            res.append(sorted2[j])
    return res
print(sortArray([-1,2,-8,-10]))