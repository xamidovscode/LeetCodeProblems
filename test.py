#1 CHI AMALIY TOPSHIRIQ

"""
1 chi misol
"""
# a = -56
# n = 50
# b = -56 % 50
# print("-56mod50 =", b)

"""
2 chi misol
"""
# def modular_inverse(e, n):
#     original_n, x, y, x1, x2 = n, 0, 1, 1, 0
#     while e > 0:
#         q, r = divmod(n, e)
#         n, e = e, r
#         x, x1 = x1 - q * x, x
#         y, x2 = x2 - q * y, y
#     return x2 % original_n if n == 1 else None
# n = 2333
# e = 60
# d = modular_inverse(e, n)
# print("(e*d)modn = 1 natija:", d)

"""
3 chi misol
"""
# def extended_gcd(a, b):
#     if b == 0:
#         return a, 1, 0
#     gcd, alpha1, beta1 = extended_gcd(b, a % b)
#     alpha = beta1
#     beta = alpha1 - (a // b) * beta1
#     return gcd, alpha, beta
#
# A = 5838
# B = 3990
#
# gcd, alpha, beta = extended_gcd(A, B)
# print(f"EKUB({A}, {B}) = {gcd}")
# print(f"alpha = {alpha}")
# print(f"beta = {beta}")

"""
4 chi misol
"""
a = 18888888881888888888188888888818888888881888888888188888888818888888881888888888188888888818888888881888888888
e = 546345345345345345345345345345345546345345345345345345345345345345546345345345345345345345345345345
n = 546345345345345345345345345345345546345345345345345345345345345345546345345345345345345345345345345546345345345345345345345345345345

result = pow(a, e, n)

print(f"{a}^{e} mod {n} = {result}")



















