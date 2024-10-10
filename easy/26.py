from django.contrib.sitemaps.views import index


class Solution:

    def remove_duplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1, nums
obj = Solution()
function = obj.remove_duplicates([1,1,2])

print(function)

