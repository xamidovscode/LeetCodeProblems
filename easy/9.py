

def isPalindrome(x):
    #SLICING METHOD
    # if x < 0: return False
    # string = str(x)
    # length = len(string)
    # if length == 1: return True
    # condition, quality = length % 2 , length // 2
    # if condition == 1:
    #     obj_1, obj_2 = string[:quality], string[quality + 1:]
    # else:
    #     obj_1, obj_2 = string[:quality], string[quality:]
    # return obj_1 == obj_2[::-1]

    #OPTIMAL METHOD
    number = str(x)
    return number == number[::-1]


a = isPalindrome(1001)
print(a)
