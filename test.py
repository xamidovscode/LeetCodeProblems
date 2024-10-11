def tublik(a):
    upper = 0
    lower = 0
    for i in a:
        if i.islower():
            lower += 1
        else:
            upper += 1
    return upper, lower


print(tublik("Salom"))