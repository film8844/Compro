""" doc """
def main(inp, key):
    """ doc """
    alpha = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ',
             'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต',
             'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย',
             'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
    vowel1 = ['ฯ', 'ะ', 'า', 'ำ', 'เ', 'แ', 'โ', 'ใ', 'ไ', 'ๅ', 'ๆ']
    vowel2 = ['ั', 'ิ', 'ี', 'ึ', 'ื', '็', '์']
    vowel3 = ['ุ', 'ู']
    tone = ['่', '้', '๊', '๋']
    num = ['๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙']
    # print(len(alpha),len(vowel1),len(vowel2),len(vowel3),len(tone),len(num))
    for i in inp:
        if i in alpha:
            print(alpha[(alpha.index(i) + key) % len(alpha)],end="")
        elif i in vowel1:
            print(vowel1[(vowel1.index(i) + key) % len(vowel1)],end="")
        elif i in vowel2:
            print(vowel2[(vowel2.index(i) + key) % len(vowel2)],end="")
        elif i in vowel3:
            print(vowel3[(vowel3.index(i) + key) % len(vowel3)],end="")
        elif i in tone:
            print(tone[(tone.index(i) + key) % len(tone)],end="")
        elif i in num:
            print(num[(num.index(i) + key) % len(num)],end="")
        else:
            print(i,end="")
main(input(), int(input()))