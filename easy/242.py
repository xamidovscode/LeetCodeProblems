

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for i in range(0, len(s)):
        obj_s = s[i]
        obj_t = t[i]
        if obj_s not in count_s:
            count_s[obj_s] = 1
        else:
            value_s = count_s[obj_s] + 1
            count_s.pop(obj_s)
            count_s[obj_s] = value_s

        if obj_t not in count_t:
            count_t[obj_t] = 1
        else:
            value_t = count_t[obj_t] + 1
            count_t.pop(obj_t)
            count_t[obj_t] = value_t
    return count_t == count_s
print(isAnagram("salom", "salom"))