
a = 0
i1 = 2
result = []
while i1 <= 1000:
    i2 = 2
    print(i1)
    while i2 <= i1:
        if i2 // i1 != 0:
            break
        result.append(i1)
        i2 += 1
    i1 += 1

print(result)