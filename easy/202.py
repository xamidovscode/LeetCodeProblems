def isHappy(n: int):
    if len(str(n)) == 1 and n != 1 and len(str(n**2)) == 1:
        return False
    verible = str(n)
    sickle = 0
    while True:
        result = 0
        for i in verible:
            obj = int(i)
            result += obj**2
        if len(str(result**2)) == 1 and result**2 != 1:
            return False
        elif result == 1:
            return True
        if result == n**2 and sickle != 0:
            return False
        verible = str(result)
        sickle += 1
        print(verible, sickle)
print(isHappy(5))