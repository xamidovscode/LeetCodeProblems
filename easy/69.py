def my_sqrt(x: int) -> int:
    condition = x
    i = 0
    result = 0
    while i <= condition:
        a = i * i
        if a <= x:
            result = i
        else:
            break
        i += 1

    return result

print(my_sqrt(5))
