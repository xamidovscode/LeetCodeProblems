

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    count2 = {}
    for i in  range(len(s)):
        count[s[i]] = 1 + count.get(s[i], 0)
        count2[t[i]] = 1 + count2.get(t[i], 0)

    return count == count2

print(isAnagram("salom", "salom"))