def convert(s: str, numRows: int) -> str:
    is_main = 0
    i = 0
    result = ''
    while i <= len(s) - 1:
        if is_main == 0:
            result = result + s[0:numRows]
            print(result)
            i += numRows
            is_main = 1
        i += 1
        print(i)
    return s

print(convert("PAYPALISHIRING", 3))
# print('PAHNAPLSIIGYIR')
