class Solution(object):
    def strStr(self, haystack, needle):
        for ind, i in enumerate(haystack):
            if haystack[ind:ind + len(needle)] == needle:
                return ind
        return -1

obj = Solution()
function = obj.strStr('hello', 'lo')

print(function)
