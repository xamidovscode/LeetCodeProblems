class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numbers = ''.join(map(str, digits))
        numbers = int(numbers) + 1
        result = [int(numb) for numb in str(numbers)]
        return result


obj = Solution()
function = obj.plusOne([1, 2, 4])

print(function)
