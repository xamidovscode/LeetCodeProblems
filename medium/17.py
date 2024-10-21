from typing import List


def letterCombinations(digits: str) -> List[str]:
    numbers = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    strs = []
    result = []
    for i in digits:
        strs.append(numbers[i])
    print(strs)
    for i1 in strs:
        for i2 in i1:
            print(i2)
    return []

print(letterCombinations("23"))