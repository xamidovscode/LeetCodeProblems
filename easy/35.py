class Solution(object):

    @classmethod
    def searchInsert(cls, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            result = nums
            result.append(target)
            return sorted(result).index(target)


obj = Solution()

function = obj.searchInsert([1, 2, 3, 4, 6], 5)

print(function)

