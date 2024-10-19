from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    result = set()
    for i in nums:
        if i not in result:
            return True
        result.add(i)

    return False


print(containsDuplicate([1, 2, 3, 4, 5, 1]))