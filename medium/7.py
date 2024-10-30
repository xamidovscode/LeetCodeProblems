

def reverse(x: int) -> int:
    if x < 0:
        result = -int(str(abs(x))[::-1])
    else:
        result = int(str(x)[::-1])
    if result not in range(-2147483648, 2147483647):
        return 0
    return result
print(reverse(-123))
