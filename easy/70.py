class Solution:

    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        first = 1
        second = 2

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second


print(Solution().climb_stairs(3))
