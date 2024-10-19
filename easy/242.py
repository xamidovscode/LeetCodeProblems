

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for i in range(0, len(s)):
        print(s[i])
print(isAnagram("salom", "aalom"))