
def my_atoi(s: str) -> int:
    result = ''
    is_plus = 1
    for i in s:
        if i == "-":
            is_plus = 0
        if i.isdigit() and i != "0":
            result = result + i
    result = int(result) if is_plus else -(int(result))
    return result

print(my_atoi("1337c0d3"))