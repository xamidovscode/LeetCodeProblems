class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        for i in s:

            if i in opening:
                opened.append(i)
            else:
                for index, value in enumerate(closing):
                    if value == i:
                        if opened == []:
                            return False
                        else:
                            last = opened.pop()
                            if opening[index] != last:
                                return False
        return (opened == [])


sol = Solution()
x = sol.isValid("[([])]")
print(x)
