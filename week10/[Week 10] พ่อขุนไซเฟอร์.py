'''doc'''


def main(thai, num):
    '''main'''
    alpha = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ',
             'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต',
             'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย',
             'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส',
             'ห', 'ฬ',
             'อ', 'ฮ']
    sarahrow = ['ฯ', 'ะ', 'า', 'ำ', 'เ', 'แ', 'โ', 'ใ', 'ไ', 'ๅ', 'ๆ']
    sarahloi = ['ั', 'ิ', 'ี', 'ึ', 'ื', '็', '์']
    sarahlang = ['ุ', 'ู']
    wannatook = ['่', '้', '๊', '๋']
    numthai = ['๐', '๑', '๒', '๓', '๔', '๔', '๕', '๖', '๗', '๘', '๙']
    for i in thai:
        if i in alpha:
            print(alpha[(alpha.index(i) + num) % (len(alpha))], end='')
        elif i in sarahrow:
            print(sarahrow[(sarahrow.index(i) + num) % len(sarahrow)], end='')
        elif i in sarahloi:
            print(sarahloi[(sarahloi.index(i) + num) % len(sarahloi)], end='')
        elif i in sarahlang:
            print(sarahlang[(sarahlang.index(i) + num) % len(sarahlang)], end='')
        elif i in wannatook:
            print(wannatook[(wannatook.index(i) + num) % len(wannatook)], end='')
        elif i in numthai:
            print(numthai[(numthai.index(i) + num) % len(numthai)], end='')
        else:
            print(i, end='')


main(input(), int(input()))
