from django.contrib.sitemaps.views import index


class Solution(object):
    @classmethod
    def remove_duplicates(cls, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = []
        k = 0
        for ind, value in enumerate(nums):
            if value not in duplicate:
                duplicate.append(value)
                k += 1
            else:
                nums[ind:ind + 1] = ["p"]

        return nums


obj = Solution()
function = obj.remove_duplicates([1, 1, 1, 2, 3])


print(function)

