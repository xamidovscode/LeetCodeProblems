def longestCommonPrefix(strs):
    for i in range(0, len(strs)):
        for j in strs:
            print(j[i])
    return True


strs = ['flower', 'flow', 'flight']
longestCommonPrefix(strs)

