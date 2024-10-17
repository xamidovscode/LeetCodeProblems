i1 = 10000
result = []

while len(result) < 10:
    i2 = 2
    while i2 <= i1 // 2:
        if i1 % i2 == 0:
            break
        i2 += 1
    else:
        result.append(i1)
    i1 += 1

print(result)
