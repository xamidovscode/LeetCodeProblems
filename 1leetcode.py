def TwoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None


nums = [3, 2, 4]
target = 6

TwoSum(nums=nums, target=target)
