class Solution:
    def longest_palindrome(self, s: str) -> str:
        rst = ""
        def get_longest_palindrome(a=None):
            if not a:
                a = s
            i1 = 0
            while i1 <= len(s) -1:
                substring1 = s[0:i1 + 1]
                print(substring1, 11111111111111)
                # if len(substring1) == 1 and len(rst) < 1:
                #     rst = substring1
                #     continue
                # i2 = 0
                # while i2 <= len(substring1) - 1:
                #     substring2 = substring1[0:i2 + 1]
                #     print(substring2)
                #     i2 += 1
                i1 += 1
            else:
                return get_longest_palindrome()
        return rst


obj = Solution()
function = obj.longest_palindrome("babad")


print(function)