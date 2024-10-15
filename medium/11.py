from typing import List



def max_area(height: List[int]) -> int:
    result = 0
    i1 = 0
    while i1 < len(height) - 1:
        objects_1 = height[i1 + 1:]
        obj = height[i1]
        for ind,i2 in enumerate(objects_1):
            length = ind - i1
            calculated = min(obj, i2) * (length if length != 0 else 1)
            if calculated > result:
                result = calculated
        i1 += 1
    return result

print(max_area([4,3,2,1,4]))

