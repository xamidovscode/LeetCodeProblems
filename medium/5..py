class Solution:
    def longest_palindrome(self, s: str) -> str:
        length = len(s)
        i1 = 0
        while i1 <= length:
            substring = s[i1:length - i1]
            print(substring)
            i1 += 1
        return s


obj = Solution()
function = obj.longest_palindrome("babad")


print(function)