class Solution(object):
    @classmethod
    def removeDuplicates(cls, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = []
        k = 0
        for i in nums:
            ind = nums.index(i)
            if i not in duplicate:
                duplicate.append(i)
                k += 1
            else:
                nums.pop(ind)

        return nums


obj = Solution()
function = obj.removeDuplicates([1, 1, 1, 2, 3])

print(function)

