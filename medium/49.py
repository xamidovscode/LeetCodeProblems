from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    for ind, i in enumerate(strs):
        strs.pop(ind)
    print(strs)
    return []


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))