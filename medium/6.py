
def convert(s: str, numRows: int) -> str:
    is_main = 0
    i = 0
    result = ''
    while i <= len(s) - 1:
        if not is_main:
            result = result + "," + s[i:numRows]
            i += numRows
            is_main = 1
        else:
            result = result + "," + s[i]
            is_main = 0
            i += 1
    return result

print(convert("PAYPALISHIRING", 3))
# print('PAHNAPLSIIGYIR')
