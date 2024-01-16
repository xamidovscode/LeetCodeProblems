# Is Palindrome Number Function
def IsPalindrome(x: int):
    s = str(x)
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


x = 121121121
IsPalindrome(x=x)

