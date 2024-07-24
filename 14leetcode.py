def longestCommonPrefix(strs):
    if not strs:
        return ""

    min_length = len(min(strs, key=len))

    prefix = ""

    for i in range(min_length):
        char = strs[0][i]

        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    print(prefix)
    return prefix


strs = ["dog", "racecar", "car"]
longestCommonPrefix(strs)
