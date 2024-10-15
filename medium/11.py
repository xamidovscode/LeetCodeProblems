from typing import List


def max_area(height: List[int]) -> int:
    result = 0
    i1 = 0
    while i1 <= len(height) - 1:
        objects_1 = height[i1:]
        print(objects_1)
        i1 += 1
    return result

print(max_area([1,8,6,2,5,4,8,3,7]))

