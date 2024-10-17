
class Solution:
    def longest_palindrome(self, s: str) -> str:
        rst = ""
        main_len = len(s)
        if all(char == s[0] for char in s):
            return s
        i0 = 0
        while i0 <= main_len - 1:
            last_index = main_len - 1 - i0
            if s[i0] != s[last_index]:
                break
            i0 += 1
        else:
            return s
        for i in range(0, main_len):
            target = s[i:]
            i1 = 0
            while i1 <= len(target) -1:
                substring1 = target[0:i1 + 1]
                subs1_len = len(substring1)
                if subs1_len == 1 and len(rst) < 1:
                    rst = substring1
                    continue
                i2 = 0
                while i2 <= subs1_len - 1:
                    last_index = subs1_len - 1 - i2
                    if substring1[i2] != substring1[last_index]:
                        break
                    i2 += 1
                else:
                    if len(rst) < subs1_len:
                        rst = substring1
                i1 += 1

        return rst


obj = Solution()
function = obj.longest_palindrome("321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123")
print(function)
# # best way
class Solution:
    def longest_palindrome(self, s: str) -> str:
        def check(l, r):
            while 0 <= l and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l, r
        n,L,R = len(s),0,0
        for i in range(2*n-1):
            if i%2: l,r= check((i-1)//2, (i+1)//2)
            else: l, r= check(i//2, i//2)
            if r-l > R-L: L, R = l,r
        return s[L+1:R]


obj = Solution()
function = obj.longest_palindrome("321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123")


print(function)