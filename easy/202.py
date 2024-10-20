
def isHappy(n: int):
    seen=set()
    curr=str(n)
    while curr not in seen:
        seen.add(curr)
        summ=0
        for digit in curr:
            summ+=int(digit)**2

        if summ ==1:
            return True
        curr=str(summ)
    return False

print(isHappy(1111111))