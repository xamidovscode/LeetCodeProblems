from typing import List

def max_area(height: List[int]) -> int:
    result = 0
    i1 = 0
    while i1 < len(height) - 1:
        obj1 = height[i1]
        objects = height[i1 + 1:]
        i2 = 0
        while i2 < len(objects):
            length = i2 + i1
            obj2 = height[i2]
            calculated = min(obj1, obj2) * (length if length != 0 else 1)
            if calculated > result:
                result = calculated
            i2 += 1
        i1 += 1
    return result

print(max_area([2,3,4,5,18,17,6]))

