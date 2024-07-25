class Solution(object):
    def strStr(self, haystack, needle):
        for num, i in enumerate(haystack):
            if i == needle[0] and haystack[num:num + len(needle)] == needle:
                return num
        return -1


obj = Solution()
function = obj.strStr('hello', 'lo')

print(function)
