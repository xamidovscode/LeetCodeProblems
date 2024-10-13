
class Solution:
    def longest_palindrome(self, s: str) -> str:
        i1 = 0
        rst = ""
        substrings = []
        for i in range(0, len(s) - 1):
            substrings.append(s[i:])
        for target in substrings:
            while i1 <= len(target) -1:
                substring1 = target[0:i1 + 1]
                if len(substring1) == 1 and len(rst) < 1:
                    rst = substring1
                    # continue
                i2 = 0
                while i2 <= len(substring1) - 1:
                    last_index = len(substring1) - 1 - i2
                    if substring1[i2] != substring1[last_index]:
                        break
                    i2 += 1
                else:
                    if len(rst) < len(substring1):
                        rst = substring1
                i1 += 1

        return rst


obj = Solution()
function = obj.longest_palindrome("qabab")


print(function)