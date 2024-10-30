def longestCommonPrefix(strs):
    if not strs:
        return ""
    s = strs[0]
    for j in strs[1:]:
        while j.find(s) != 0:
            s = s[:-1]
            if not s:
                return ""
    return s


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
