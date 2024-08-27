class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(cls, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        left = 0
        max_length = 0

        for i in range(len(s)):
            if s[i] in last_seen and last_seen[s[i]] >= left:
                left = last_seen[s[i]] + 1

            last_seen[s[i]] = i

            max_length = max(max_length, i - left + 1)

        return max_length


obj = Solution()
function = obj.lengthOfLongestSubstring("abcabcbb")

print(function)
