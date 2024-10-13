
def convert(s: str, numRows: int) -> str:
    is_main = 0
    i = 0
    result = ''
    while i <= len(s) - 1:
        if is_main == 0:
            result = result + "," + s[0:numRows]
            i += numRows - 1
            is_main = 1
        else:
            result = result + "," + s[i:i + 1]
            is_main = 0
            i += 2
        i += 1
    return result

print(convert("PAYPALISHIRING", 3))
# print('PAHNAPLSIIGYIR')
