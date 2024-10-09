from django.contrib.sitemaps.views import index


class Solution(object):
    @classmethod
    def remove_duplicates(cls, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        i = 0
        print("First", nums)
        while i <= len(nums) - 1:
            element = nums[i]
            if element not in unique:
                unique.append(element)
            else:
                nums.pop(i)
                print(i, nums)
            i += 1
        return i, unique, nums


obj = Solution()
function = obj.remove_duplicates([0,0,1,1,1,2,2,3,3,4])


print(function)

