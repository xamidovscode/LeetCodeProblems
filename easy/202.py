def isHappy(n: int):
    if len(str(n)) == 1 and n != 1 and len(str(n**2)) == 1:
        return False
    verible = str(n**2)
    sickle = 0
    objects = []
    while True:
        result = 0
        if verible in objects:
            return False
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
        objects.append(verible)
        sickle += 1
print(isHappy(5))