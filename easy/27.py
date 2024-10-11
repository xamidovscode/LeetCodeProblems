class Solution:
    @classmethod
    def removeElement(cls, nums, val) -> int:
        index = 0
        k = 0
        for i in nums:
            if i == val:
                nums.pop(index)
                nums.insert(index, '_')
                k += 1
            index += 1
        return k, nums


print(Solution.removeElement([3, 2, 2, 3], 3))
