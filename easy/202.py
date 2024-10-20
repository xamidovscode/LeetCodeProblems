
def isHappy(n: int):
    if len(str(n)) == 1 and n != 1 and len(str(n**2)) == 1:
        return False
    obj = str(n)
    while True:
        result = 0
        for i in obj:
            result += int(i)**2
        if result == 1:
            return True
        if result in (5, 4):
            return False
        obj = str(result)

print(isHappy(1111111))