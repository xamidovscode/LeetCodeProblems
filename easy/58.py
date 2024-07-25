class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])



obj = Solution()
function = obj.lengthOfLastWord("   fly me   to   the moon  ")

print(function)

