

def reverse(x: int) -> int:
    y = str(x)
    result = ''
    is_plus = 1
    if x not in range(-8463947412, 7463847412):
        return 0

    for i in y:
        if i == "-":
            is_plus = 0
        else:
            result = i + result
    result = int(result)
    return result if is_plus else -result

print(reverse(123))
