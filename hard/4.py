class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # objects = sorted(nums1 + nums2)
        # objects = objects[1:][:-1]
        # return round(sum(objects) / len(objects), 5)
        objects = [nums1 + nums2]
        mx = max(objects[0])
        mn = min(objects[0])
        result = 0
        length = 0
        for i in objects[0]:
            if i != mn and i != mx:
                result += i
                length += 1
        return round((result / length), 5)


obj = Solution()
function = obj.findMedianSortedArrays([1, 2], [3, 4])

print(function)
