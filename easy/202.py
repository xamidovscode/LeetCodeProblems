def isHappy(n: int):
    if len(str(n)) == 1 and n != 1 and len(str(n**2)) == 1:
        return False
    return True
print(isHappy(5))