

def reverse(x: int) -> int:
    y = str(x)
    result = ''
    is_plus = 1
    for i in y:
        if i == "-":
            is_plus = 0
        else:
            result = i + result
    result = int(result)
    if result not in range(-2147483648, 2147483647):
        return 0
    return result if is_plus else -result

print(reverse(-123))
