def isPalindrome(x):
    x = str(x)
    for i in range(0, len(x)):
        result = x[i] == x[len(x) - i - 1]
        if result is False:
            return False
    return True


a = isPalindrome(121)
print(a)
