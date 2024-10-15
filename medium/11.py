from typing import List

def max_area(height: List[int]) -> int:
    result = 0
    i1 = 0
    main_len = len(height)
    while i1 < main_len - 1:
        obj1 = height[i1]
        i2 = i1 + 1
        while i2 < main_len:
            length = i2 - i1
            obj2 = height[i2]
            calculated = (obj1 if obj1 < obj2 else obj2) * length
            if calculated > result:
                result = calculated
            i2 += 1
        i1 += 1
    return result

print(max_area([2,3,4,5,18,17,6]))

