from typing import List

from typing import List

def max_area(height: List[int]) -> int:
    result = 0
    i1, i2 = 0, len(height) - 1

    while i1 < i2:
        width = i2 - i1
        min_height = min(height[i1], height[i2])
        calculated = width * min_height
        result = max(result, calculated)

        if height[i1] < height[i2]:
            i1 += 1
        else:
            i2 -= 1

    return result


print(max_area([2,3,4,5,18,17,6]))

