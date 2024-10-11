
def add_binary(a: str, b: str) -> str:
    a=int(a,2) # ikkilikdan 10 likka otish bo'ldi
    b=int(b,2)
    a = a + b
    st =""
    if a+b ==0: return "0"
    while a!=0:
        st = str(a%2)+ st
        print(a)
        a = a//2

    return st



print(add_binary("111", "101"))